# =========================
# 📄 UI 控件模块
# =========================

import ipywidgets as widgets

def section_title(text):
    """定义每个部分标题样式"""
    return widgets.HTML(value=f"<h4 style='color:navy'>{text}</h4>")

# === 表头区域信息 ===
beginning_date = widgets.Text(description="beginning date")
ending_date = widgets.Text(description="ending date")
ending_year = widgets.Text(description="ending year(last two number 20__)")

# === 基本身份信息 ===
first_name = widgets.Text(description="first_name")
last_name = widgets.Text(description="last_name")
ssn = widgets.Text(description="SSN")

# === 居住地址 ===
residence_address = widgets.Text(description="Address in country of residence")
us_address = widgets.Text(description="Address in the United States")

# === 签证信息 ===
visa_type = widgets.Text(description="visa_type")
Current_nonimmigrant_status = widgets.Text(description="Current nonimmigrant status")
citizenship = widgets.Text(description="country of citizenship")
passport_country = widgets.Text(description="passport_country")
passport_number = widgets.Text(description="passport_number")

# === 出入境天数 ===
days_2024 = widgets.IntText(description="days in USA_2024")
days_2023 = widgets.IntText(description="days in USA_2023")
days_2022 = widgets.IntText(description="days in USA_2022")
exclude_days = widgets.IntText(description="exclude_days")

# === 教师/培训人员信息（Part II）===
teacher_name_2024 = widgets.Text(description="teacher_name_2024")
teacher_address_2024 = widgets.Text(description="teacher_address_2024")
teacher_phone_2024 = widgets.Text(description="teacher_phone_2024")

trainee_director_name_2024 = widgets.Text(description="trainee_director_name_2024")
trainee_director_address_2024 = widgets.Text(description="trainee_director_address_2024")
trainee_director_phone_2024 = widgets.Text(description="trainee_director_phone_2024")

visa_2018 = widgets.Text(description="visa_2018 (J/Q)")
visa_2019 = widgets.Text(description="visa_2019 (J/Q)")
visa_2020 = widgets.Text(description="visa_2020 (J/Q)")
visa_2021 = widgets.Text(description="visa_2021 (J/Q)")
visa_2022 = widgets.Text(description="visa_2022 (J/Q)")
visa_2023 = widgets.Text(description="visa_2023 (J/Q)")

exempt_as_teacher_or_trainee = widgets.RadioButtons(
    options=["Yes", "No"],
    description="Exempt as Teacher/Trainee",
    style={'description_width': 'initial'}
)

# === 学校/学生信息（Part III）===
school_name_in_2024 = widgets.Text(description="school_name in 2024")
school_phone_in_2024 = widgets.Text(description="school_phone in 2024")
school_address_in_2024 = widgets.Text(description="school_address in 2024")

director_name_in_2024 = widgets.Text(description="director_name in 2024")
director_phone_in_2024 = widgets.Text(description="director_phone in 2024")
director_address_in_2024 = widgets.Text(description="director_address in 2024")

type_of_U_S_visa_F_J_M_or_Q_in_2018 = widgets.Text(description="visa (F/J/M/Q) 2018")
type_of_U_S_visa_F_J_M_or_Q_in_2019 = widgets.Text(description="visa (F/J/M/Q) 2019")
type_of_U_S_visa_F_J_M_or_Q_in_2020 = widgets.Text(description="visa (F/J/M/Q) 2020")
type_of_U_S_visa_F_J_M_or_Q_in_2021 = widgets.Text(description="visa (F/J/M/Q) 2021")
type_of_U_S_visa_F_J_M_or_Q_in_2022 = widgets.Text(description="visa (F/J/M/Q) 2022")
type_of_U_S_visa_F_J_M_or_Q_in_2023 = widgets.Text(description="visa (F/J/M/Q) 2023")

exempt_as_student = widgets.RadioButtons(
    options=["Yes", "No"],
    description="Exempt as Student?",
    style={'description_width': 'initial'}
)

green_card_applied = widgets.RadioButtons(
    options=["Yes", "No"],
    description="Green Card Applied?",
    style={'description_width': 'initial'}
)

green_card_explanation = widgets.Textarea(
    description="Explanation (Line 14)",
    placeholder="If Yes to Green Card, explain here...",
    layout=widgets.Layout(width="100%", height="100px"),
    style={'description_width': 'initial'}
)

# === 运动员信息（Part IV）===
charitable_event_name_1 = widgets.Text(description="Charity Event 1")
charitable_event_name_2 = widgets.Text(description="Charity Event 2")
charitable_event_name_3 = widgets.Text(description="Charity Event 3")

charitable_org_1 = widgets.Text(description="Charity Org 1")
charitable_org_2 = widgets.Text(description="Charity Org 2")
charitable_org_3 = widgets.Text(description="Charity Org 3")

# === 医疗问题豁免（Part V）===
medical_condition_line1 = widgets.Text(description="Condition (Line 1)")
medical_condition_line2 = widgets.Text(description="Condition (Line 2)")
medical_condition_line3 = widgets.Text(description="Condition (Line 3)")
medical_condition_line4 = widgets.Text(description="Condition (Line 4)")

intended_departure_date = widgets.Text(description="Intended Leave Date")
actual_departure_date = widgets.Text(description="Actual Leave Date")
physician_certify_name = widgets.Text(description="Name of Taxpayer")
physician_name = widgets.Text(description="Physician's Name")
physician_address_and_phone = widgets.Text(description="Physician Contact")

# === 控制区控件 ===
w2_pdf_path = widgets.Text(description="W-2 PDF Path")
template_path = widgets.Text(description="8843 Template")
gpt_button = widgets.Button(description="🧠 Extract W-2")
submit_button = widgets.Button(description="📝 Generate 8843")
gpt_json_output = widgets.Textarea(value="", description="GPT JSON", layout=widgets.Layout(width="100%", height="200px"))