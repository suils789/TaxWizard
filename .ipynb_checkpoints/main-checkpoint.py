# =========================
# ▶️ 程序主入口 main.py
# =========================

import os
import json
import pprint
import w2_extractor  # 从 W-2 中提取字段
import form_8843_filler  # 填充和生成 8843 PDF
import ui_widgets as ui  # 定义所有 UI 控件
import ui_layout  # 组装表单界面
from IPython.display import display
from constants import DEFAULT_W2_PDF_PATH, DEFAULT_8843_TEMPLATE_PATH


def on_extract_w2(btn):
    """
    当点击 🧠 Extract W-2 按钮时触发：
    1. 检查文件路径；
    2. 调用 GPT 提取信息；
    3. 自动填入基本字段；
    4. 显示预览，保存 json。"""
    if not os.path.exists(ui.w2_pdf_path.value):
        print("❌ 找不到 W2 文件路径，请检查路径！")
        return

    print("🧠 正在提取 W-2 信息 ...")
    img_path = w2_extractor.pdf_to_image(ui.w2_pdf_path.value)
    gpt_json = w2_extractor.extract_w2_fields_via_gpt(img_path)

    ui.gpt_json_output.value = json.dumps(gpt_json, indent=2, ensure_ascii=False)
    w2_extractor.display_preview_images([ui.w2_pdf_path.value], "📎 上传的 W-2")

    try:
        result = gpt_json


        global w2_data
        w2_data = result

        with open("w2_data.json", "w") as f:
            json.dump(w2_data, f, indent=2)
        print("✅ 已保存 W-2 数据至 w2_data.json")

    except Exception as e:
        print("❌ W-2 JSON 处理失败：", e)


def on_submit(btn):
    """
    当点击 Generate 8843 按钮时触发：
    1. 收集表单所有字段；
    2. 构建 merged_data；
    3. 调用填表函数生成 PDF。
    """
    merged_data = {
        "beginning date": ui.beginning_date.value,
        "ending date": ui.ending_date.value,
        "ending year(last two number 20__)": ui.ending_year.value,
        "first_name": ui.first_name.value,
        "last_name": ui.last_name.value,
        "TIN": ui.ssn.value,
        "Address in country of residence": ui.residence_address.value,
        "Address in the United States": ui.us_address.value,
        "visa_type": ui.visa_type.value,
        "Current nonimmigrant status": ui.Current_nonimmigrant_status.value,
        "country of citizenship": ui.citizenship.value,
        "passport_country": ui.passport_country.value,
        "passport_number": ui.passport_number.value,
        "days in USA_2024": ui.days_2024.value,
        "days in USA_2023": ui.days_2023.value,
        "days in USA_2022": ui.days_2022.value,
        "exclude_days": ui.exclude_days.value,
        "teacher_name_2024": ui.teacher_name_2024.value,
        "teacher_address_2024": ui.teacher_address_2024.value,
        "teacher_phone_2024": ui.teacher_phone_2024.value,
        "trainee_director_name_2024": ui.trainee_director_name_2024.value,
        "trainee_director_address_2024": ui.trainee_director_address_2024.value,
        "trainee_director_phone_2024": ui.trainee_director_phone_2024.value,
        "visa_2018": ui.visa_2018.value,
        "visa_2019": ui.visa_2019.value,
        "visa_2020": ui.visa_2020.value,
        "visa_2021": ui.visa_2021.value,
        "visa_2022": ui.visa_2022.value,
        "visa_2023": ui.visa_2023.value,
        "exempt_as_teacher_or_trainee_yes": (
            "Yes" if ui.exempt_as_teacher_or_trainee.value == "Yes" else ""
        ),
        "exempt_as_teacher_or_trainee_no": (
            "Yes" if ui.exempt_as_teacher_or_trainee.value == "No" else ""
        ),
        "school_name in 2024": ui.school_name_in_2024.value,
        "school_phone in 2024": ui.school_phone_in_2024.value,
        "school_address in 2024": ui.school_address_in_2024.value,
        "director_name in 2024": ui.director_name_in_2024.value,
        "director_phone in 2024": ui.director_phone_in_2024.value,
        "director_address in 2024": ui.director_address_in_2024.value,
        "type of U.S. visa (F, J, M, or Q) in 2018": ui.type_of_U_S_visa_F_J_M_or_Q_in_2018.value,
        "type of U.S. visa (F, J, M, or Q) in 2019": ui.type_of_U_S_visa_F_J_M_or_Q_in_2019.value,
        "type of U.S. visa (F, J, M, or Q) in 2020": ui.type_of_U_S_visa_F_J_M_or_Q_in_2020.value,
        "type of U.S. visa (F, J, M, or Q) in 2021": ui.type_of_U_S_visa_F_J_M_or_Q_in_2021.value,
        "type of U.S. visa (F, J, M, or Q) in 2022": ui.type_of_U_S_visa_F_J_M_or_Q_in_2022.value,
        "type of U.S. visa (F, J, M, or Q) in 2023": ui.type_of_U_S_visa_F_J_M_or_Q_in_2023.value,
        "exempt_as_student_yes": "Yes" if ui.exempt_as_student.value == "Yes" else "",
        "exempt_as_student_no": "Yes" if ui.exempt_as_student.value == "No" else "",
        "green_card_applied_yes": "Yes" if ui.green_card_applied.value == "Yes" else "",
        "green_card_applied_no": "Yes" if ui.green_card_applied.value == "No" else "",
        "green_card_explanation_1": (
            ui.green_card_explanation.value.split("\\n")[0]
            if ui.green_card_explanation.value
            else ""
        ),
        "green_card_explanation_2": (
            ui.green_card_explanation.value.split("\\n")[1]
            if len(ui.green_card_explanation.value.split("\\n")) > 1
            else ""
        ),
        "green_card_explanation_3": (
            ui.green_card_explanation.value.split("\\n")[2]
            if len(ui.green_card_explanation.value.split("\\n")) > 2
            else ""
        ),
        "charitable_event_name_1": ui.charitable_event_name_1.value,
        "charitable_event_name_2": ui.charitable_event_name_2.value,
        "charitable_event_name_3": ui.charitable_event_name_3.value,
        "charitable_org_1": ui.charitable_org_1.value,
        "charitable_org_2": ui.charitable_org_2.value,
        "charitable_org_3": ui.charitable_org_3.value,
        "medical_condition_line1": ui.medical_condition_line1.value,
        "medical_condition_line2": ui.medical_condition_line2.value,
        "medical_condition_line3": ui.medical_condition_line3.value,
        "medical_condition_line4": ui.medical_condition_line4.value,
        "intended_departure_date": ui.intended_departure_date.value,
        "actual_departure_date": ui.actual_departure_date.value,
        "physician_certify_name": ui.physician_certify_name.value,
        "physician_name": ui.physician_name.value,
        "physician_address_and_phone": ui.physician_address_and_phone.value,
    }

    print("📟 merged_data 内容预览：")
    pprint.pprint(merged_data, sort_dicts=False)

    form_8843_filler.fill_8843_pdf(merged_data, ui.template_path.value)
    print("✅ 填表完成，生成 PDF")


def main():
    ui.gpt_button.on_click(on_extract_w2)
    ui.submit_button.on_click(on_submit)
    display(ui_layout.build_form_sections())


if __name__ == "__main__":
    main()
