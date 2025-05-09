# =========================
# 📄 Form 8843 PDF Filler
# =========================

import os
from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName
import fitz
from IPython.display import display, Image
from pdf2image import convert_from_path
from constants import form_8843_fields_map, DEFAULT_8843_TEMPLATE_PATH, DEFAULT_OUTPUT_PDF_PATH

###可以删掉
def flatten_pdf(input_path, output_path):
    """Flatten PDF by cleaning up dynamic fields"""
    doc = fitz.open(input_path)
    for page in doc:
        page.clean_contents()
    doc.save(output_path)

## 填充8843 form
 """参数：
    - merged_data：字典，逻辑字段名 -> 填写值
    - template_path：表单模板路径（默认从 constants 读取）
    - output_path：生成的 PDF 存储路径"""

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
                    #查找当前字段是否在映射中
                    for logical_name, pdf_field in form_8843_fields_map.items():
                        if pdf_field == key_str and logical_name in merged_data:
                            value = merged_data[logical_name]
                            # ✅ 如果是 checkbox（c1_ 开头），根据值 Yes / No 设置打勾状态
                            if key_str.startswith("c1_"):
                                annotation.update(PdfDict(AS=PdfName("Yes" if value == "Yes" else "Off")))
                            else:
                                annotation.update(PdfDict(V=str(value)))
    #写入新PDF
    PdfWriter(output_path, trailer=pdf).write()

    # 生成Flatten版本 & Save，并预览图片
    flatten_pdf(output_path, output_path.replace(".pdf", "_flat.pdf"))
    display_preview_images([output_path.replace(".pdf", "_flat.pdf")], "📄 生成的 Form 8843")

# 将 PDF 转换为 PNG 图像并显示（仅显示第一页，方便 Notebook 中查看结果）
def display_preview_images(pdf_paths, title="PDF Preview"):
    print(title)
    for pdf in pdf_paths:
        images = convert_from_path(pdf, dpi=100)
        for img in images[:1]:  # 每个 PDF 只显示第一页
            img_path = f"preview_{os.path.basename(pdf).split('.')[0]}.png"
            img.save(img_path)
            display(Image(filename=img_path))
