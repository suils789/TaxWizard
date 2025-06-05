# main_1040.py

# =============================
# 🧾 main_1040.py
# IRS Form 1040 自动填表主入口
# =============================

import os
import json
from IPython.display import display
import ipywidgets as widgets

from ui_widgets_1040 import *  # 所有控件和控件字典
from ui_layout_1040 import layout_1040
from constants import form_1040_fields_map
import w2_extractor
from form_1040_filler import fill_1040_pdf
from constants import DEFAULT_W2_PDF_PATH, DEFAULT_1040_TEMPLATE_PATH
import ui_widgets_1040 as ui_1040


# 1️⃣ 提取 W-2 按钮逻辑
def on_extract_w2(btn):
    if not os.path.exists(ui_1040.w2_pdf_path.value):
        print("❌ 找不到 W2 文件路径，请检查路径！")
        return

    print("🧠 正在提取 W-2 信息 ...")
    img_path = w2_extractor.pdf_to_image(ui_1040.w2_pdf_path.value)
    gpt_json = w2_extractor.extract_w2_fields_via_gpt(img_path)

    ui_1040.gpt_json_output.value = json.dumps(gpt_json, indent=2, ensure_ascii=False)
    w2_extractor.display_preview_images([ui_1040.w2_pdf_path.value], "📎 上传的 W-2")

    try:
        result = gpt_json
        line_1a.value = float(result.get("box_1", 0))
        line_25a.value = float(result.get("box_2", 0))
        print("✅ 自动填入 Line 1a 和 25a")

        global w2_data
        w2_data = result

        with open("w2_data.json", "w") as f:
            json.dump(w2_data, f, indent=2)
        print("✅ 已保存 W-2 数据至 w2_data.json")

    except Exception as e:
        print("❌ W-2 JSON 处理失败：", e)


# 2️⃣ 生成 1040 按钮逻辑
def on_generate_1040(btn=None):
    print("📥 正在收集控件数据...")
    logical_input = {
        key: (
            widget.value
            if not isinstance(widget, widgets.Checkbox)
            else ("Yes" if widget.value else "Off")
        )
        for key, widget in manual_input_1040_widgets.items()
    }
    # ✅ 特殊处理 digital_assets 的单选按钮值（Yes/No → 两个复选框字段）
    if "digital_assets" in logical_input:
        val = logical_input["digital_assets"]
        logical_input["digital_assets_yes"] = "Yes" if val == "Yes" else "Off"
        logical_input["digital_assets_no"] = "Yes" if val == "No" else "Off"
        
    # 👇 获取 Filing Status 选择值
    filing_val = logical_input.get("filing_status")

    # 👇 根据选择值，补充勾选的字段（只打一个勾）
    filing_status_map = {
        "Single": "filing_status_Single",
        "Married filing jointly": "filing_status_Married filing jointly (even if only one had income)",
        "Married filing separately": "filing_status_Married filing separately",
        "Head of household": "filing_status_Head of household",
        "Qualifying surviving spouse": "filing_status_Qualifying surviving spouse"
    }

    # ✅ 将所有 Filing Status 项清空为 Off，然后选中的设置为 Yes
    for logical_key in filing_status_map.values():
        logical_input[logical_key] = "Off"
    if filing_val in filing_status_map:
        logical_input[filing_status_map[filing_val]] = "Yes"

    print("📌 用户填写字段内容如下：")
    for k, v in logical_input.items():
        print(f" - {k} = {v}")

    print("🔄 正在映射为 PDF 字段...")
    pdf_input = {}
    for logical_key, val in logical_input.items():
        if logical_key in form_1040_fields_map:
            pdf_field = form_1040_fields_map[logical_key]
            pdf_input[pdf_field] = val
            print(f"🔧 {logical_key} → {pdf_field} → {val}")

    print("🧾 正在填充 PDF 表单...")
    fill_1040_pdf(pdf_input, template_path.value, output_path.value)

    print("✅ 1040 表格已生成：", output_path.value)


# 3️⃣ 按钮绑定
gpt_button.on_click(on_extract_w2)
generate_button.on_click(on_generate_1040)


# 4️⃣ 主函数封装
def main_1040():
    display(layout_1040)


# 5️⃣ 支持命令行直接运行
if __name__ == "__main__":
    main_1040()
