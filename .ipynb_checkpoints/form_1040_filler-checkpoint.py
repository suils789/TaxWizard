# ============================
# 🧾 IRS Form 1040 PDF Filler
# ============================

import os
import fitz  # PyMuPDF，用于 flatten
from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName, PdfObject
from pdf2image import convert_from_path
from IPython.display import display, Image

from constants import DEFAULT_1040_TEMPLATE_PATH, DEFAULT_OUTPUT_PDF_PATH_1040


def flatten_pdf(input_path, output_path):
    """将 PDF 扁平化，使填写的字段转为页面内容"""
    doc = fitz.open(input_path)
    for page in doc:
        page.clean_contents()
    doc.save(output_path)


def display_preview_images(pdf_paths, title="PDF Preview"):
    """将 PDF 转图像并在 Notebook 中展示（第一页）"""
    print(title)
    for pdf in pdf_paths:
        images = convert_from_path(pdf, dpi=100, poppler_path="/usr/local/bin")  # macOS
        for img in images[:1]:
            img_path = f"preview_{os.path.basename(pdf).split('.')[0]}.png"
            img.save(img_path)
            display(Image(filename=img_path))


def fill_1040_pdf(filled_data, template_path=DEFAULT_1040_TEMPLATE_PATH, output_path=DEFAULT_OUTPUT_PDF_PATH_1040):
    """
    自动填充 IRS Form 1040 表单，并扁平化为预览图
    - filled_data: {pdf_field_name: value}
    """
    # 1️⃣ 加载模板 PDF
    template_pdf = PdfReader(template_path)

    # ✅ 设置 NeedAppearances
    if template_pdf.Root.AcroForm:
        template_pdf.Root.AcroForm.update(PdfDict(NeedAppearances=PdfObject("true")))

    print("📝 正在填充字段:")
    for page in template_pdf.pages:
        if "/Annots" not in page:
            continue
        for annot in page["/Annots"]:
            if annot["/Subtype"] == "/Widget" and "/T" in annot:
                field_key = annot["/T"][1:-1]  # 去掉括号
                val = filled_data.get(field_key, "")

                print(f"🔧 {field_key} ← {val}")

                # ✅ 处理复选框 / 单选框（Yes/Off）
                if isinstance(val, str) and val in ["Yes", "Off"]:
                    annot.update(PdfDict(V=PdfName(val), AS=PdfName(val), Ff=1))

                # ✅ Filing Status 单选框：字段名如 c1_3[0]～c1_3[4]
                elif field_key.startswith("c1_3[") and isinstance(val, str):
                    # val 可能是 "Head of household" 等，匹配正确的选项才勾选
                    if val.strip().lower() in field_key.lower():
                        annot.update(PdfDict(V=PdfName("Yes"), AS=PdfName("Yes"), Ff=1))
                    else:
                        annot.update(PdfDict(V=PdfName("Off"), AS=PdfName("Off"), Ff=1))

                # ✅ 其余字段：文本输入
                else:
                    try:
                        annot.update(PdfDict(V=PdfObject(f"({val})"), Ff=1))
                    except Exception as e:
                        print(f"⚠️ 处理字段 {field_key} 时出错: {e}")

    # 3️⃣ 写入未扁平化 PDF
    PdfWriter(output_path, trailer=template_pdf).write()
    print(f"✅ 已保存填写后的 PDF：{output_path}")

    # 4️⃣ 扁平化 PDF
    flat_output = output_path.replace(".pdf", "_flat.pdf")
    flatten_pdf(output_path, flat_output)

    # 5️⃣ 显示 PDF 预览图（第一页）
    print(f"📎 扁平化版本：{flat_output}")
    display_preview_images([flat_output], title="📄 Flattened Form 1040（第一页预览）")
