# =========================
# 📄 Form 8843 PDF Filler
# =========================

import os
from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName
import fitz
from IPython.display import display, Image
from pdf2image import convert_from_path
from constants import form_8843_fields_map, DEFAULT_8843_TEMPLATE_PATH, DEFAULT_OUTPUT_PDF_PATH

def flatten_pdf(input_path, output_path):
    """Flatten PDF by cleaning up dynamic fields"""
    doc = fitz.open(input_path)
    for page in doc:
        page.clean_contents()
    doc.save(output_path)

def fill_8843_pdf(merged_data, template_path=DEFAULT_8843_TEMPLATE_PATH, output_path=DEFAULT_OUTPUT_PDF_PATH):
    """
    填写 Form 8843 PDF 模板，
    merged_data 是 key: value 的映射（逻辑字段 -> 填写内容）
    """
    pdf = PdfReader(template_path)
    for page in pdf.pages:
        if "/Annots" in page:
            for annotation in page["/Annots"]:
                key = annotation.get("/T")
                if key:
                    key_str = key.to_unicode()
                    for logical_name, pdf_field in form_8843_fields_map.items():
                        if pdf_field == key_str and logical_name in merged_data:
                            value = merged_data[logical_name]
                            # ✅ 如果是 checkbox（复选框），用 AS 属性打勾
                            if key_str.startswith("c1_"):
                                annotation.update(PdfDict(AS=PdfName("Yes" if value == "Yes" else "Off")))
                            else:
                                annotation.update(PdfDict(V=str(value)))

    PdfWriter(output_path, trailer=pdf).write()

    # Flatten & Save
    flatten_pdf(output_path, output_path.replace(".pdf", "_flat.pdf"))
    display_preview_images([output_path.replace(".pdf", "_flat.pdf")], "📄 生成的 Form 8843")

def display_preview_images(pdf_paths, title="PDF Preview"):
    """将 PDF 转成图片预览展示（for Notebook）"""
    print(title)
    for pdf in pdf_paths:
        images = convert_from_path(pdf, dpi=100)
        for img in images[:1]:  # 每个 PDF 只显示第一页
            img_path = f"preview_{os.path.basename(pdf).split('.')[0]}.png"
            img.save(img_path)
            display(Image(filename=img_path))
