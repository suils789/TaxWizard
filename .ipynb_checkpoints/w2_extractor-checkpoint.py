# =========================
# 📦 W2 Fields Extractor (via GPT)
# =========================

import base64
import json
import os
import re
from openai import OpenAI
from constants import OPENAI_API_KEY
from constants import DEFAULT_W2_DATA_JSON
from pdf2image import convert_from_path
from IPython.display import display, Image

# 将 PDF 文件转为图像，提交给 GPT 进行识别
def pdf_to_image(pdf_path, page_number=0):
    """Convert PDF (first page) to PNG image for GPT extraction"""
    images = convert_from_path(pdf_path, dpi=200, poppler_path="/usr/local/bin")
    image_path = "w2_temp_image.png" 
    images[page_number].save(image_path, format="PNG")  
    return image_path

# 初始化 OpenAI 客户端
client = OpenAI(api_key=OPENAI_API_KEY)

# 将图片转为 base64 编码，用于 OpenAI 的图像输入格式
def encode_image_base64(image_path):
    """把图片文件编码为 Base64 字符串"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
        
# 从 GPT 输出的 Markdown 内容中提取 JSON 部分
def extract_json_from_markdown(gpt_output):
    """从 GPT 返回的 Markdown 中提取 JSON 部分"""
    gpt_output = gpt_output.strip()

    match = re.search(r"```(?:json)?\s*(\{.*\})\s*```", gpt_output, re.DOTALL)
    if match:
        return match.group(1)

    if gpt_output.startswith("```") and gpt_output.endswith("```"):
        gpt_output = gpt_output[3:-3].strip()
        if gpt_output.lower().startswith("json"):
            gpt_output = gpt_output[4:].strip()

    return gpt_output

# 通过 GPT-4o 模型从上传的 W-2 表单截图中提取结构化字段，并定义所需字段
def extract_w2_fields_via_gpt(image_path):
    """
    上传 W-2 表单截图给 GPT，
    返回提取的结构化字段 JSON。
    """
    base64_image = encode_image_base64(image_path)
    prompt = '''You are a tax assistant. Please extract the following fields from the uploaded W-2 tax form:
- first_name
- last_name
- ssn: Social Security Number (employee)
- box_1 through box_20 (all if available)
- box_12a~12d with code + value
- box_13_statutory_employee, box_13_retirement_plan, box_13_third_party_sick_pay
- box_14: label + value
- employer_name, employer_address, employer_ein
- employee_address
Return a JSON object with all fields and keep empty if not available.'''

    # 调用 OpenAI 的 gpt-4o 图像模型
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                ]
            }
        ],
        temperature=0,
        max_tokens=1000
    )
    gpt_content = response.choices[0].message.content
    print("🔍 GPT 原始返回：", gpt_content)

    # 提取出 JSON 字符串，解析为dict
    cleaned_json = extract_json_from_markdown(gpt_content)
    return json.loads(cleaned_json)

# 用于在 Notebook 中展示 PDF 文件的第一页预览图
def display_preview_images(pdf_paths, title="PDF Preview"):
    """将 PDF 转成图片预览展示（for Notebook）"""
    print(title)
    for pdf in pdf_paths:
        images = convert_from_path(pdf, dpi=100, poppler_path="/usr/local/bin")
        for img in images[:1]:  # 每个 PDF 只显示第一页
            img_path = f"preview_{os.path.basename(pdf).split('.')[0]}.png"
            img.save(img_path)
            display(Image(filename=img_path))