# =========================
# 📄 布局模块（把ui_widgets.py 中定义的所有控件组合成一个完整的页面结构，方便用户分模块填写）
# =========================

from ipywidgets import VBox
import ui_widgets as ui

def build_form_sections():
    """把所有的 Section 按顺序组合成一个完整的表单界面"""
    return VBox([
        ui.section_title("📄 Header Info"),
        ui.beginning_date, ui.ending_date, ui.ending_year,
        
        ui.section_title("👤 Basic Identity Information (From W-2)"),
        ui.first_name, ui.last_name, ui.ssn,
        
        ui.section_title("📍 Address Information"),
        ui.residence_address, ui.us_address,
        
        ui.section_title("🛂 Visa and Immigration Info"),
        ui.visa_type, ui.Current_nonimmigrant_status, ui.citizenship, ui.passport_country, ui.passport_number,
        
        ui.section_title("📅 Days Present in the U.S."),
        ui.days_2024, ui.days_2023, ui.days_2022, ui.exclude_days,
        
        ui.section_title("👨‍🏫 Teacher/Trainee Information (Part II)"),
        ui.teacher_name_2024, ui.teacher_address_2024, ui.teacher_phone_2024,
        ui.trainee_director_name_2024, ui.trainee_director_address_2024, ui.trainee_director_phone_2024,
        ui.visa_2018, ui.visa_2019, ui.visa_2020, ui.visa_2021, ui.visa_2022, ui.visa_2023,
        ui.exempt_as_teacher_or_trainee,
        
        ui.section_title("🎓 School Information (Part III - Students)"),
        ui.school_name_in_2024, ui.school_phone_in_2024, ui.school_address_in_2024,
        ui.director_name_in_2024, ui.director_phone_in_2024, ui.director_address_in_2024,
        
        ui.section_title("📜 Visa History (F/J/M/Q Types - Part III Line 11)"),
        ui.type_of_U_S_visa_F_J_M_or_Q_in_2018,
        ui.type_of_U_S_visa_F_J_M_or_Q_in_2019,
        ui.type_of_U_S_visa_F_J_M_or_Q_in_2020,
        ui.type_of_U_S_visa_F_J_M_or_Q_in_2021,
        ui.type_of_U_S_visa_F_J_M_or_Q_in_2022,
        ui.type_of_U_S_visa_F_J_M_or_Q_in_2023,
        
        ui.section_title("❓ Special Exemptions & Green Card Status (Part III Line 12-14)"),
        ui.exempt_as_student,
        ui.green_card_applied,
        ui.green_card_explanation,
        
        ui.section_title("🏅 Charitable Events (Part IV - Athletes)"),
        ui.charitable_event_name_1, ui.charitable_event_name_2, ui.charitable_event_name_3,
        ui.charitable_org_1, ui.charitable_org_2, ui.charitable_org_3,
        
        ui.section_title("🏥 Medical Condition (Part V)"),
        ui.medical_condition_line1, ui.medical_condition_line2, ui.medical_condition_line3, ui.medical_condition_line4,
        ui.intended_departure_date, ui.actual_departure_date,
        ui.physician_certify_name, ui.physician_name, ui.physician_address_and_phone,
        
        ui.section_title("🧠 W-2 Extraction & 8843 Submit"),
        ui.w2_pdf_path, ui.template_path, ui.gpt_button, ui.submit_button,
        ui.gpt_json_output
    ])