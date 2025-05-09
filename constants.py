# =========================
# 📜 Constants and Settings
# =========================
#本 文件用于集中管理项目中使用到的常量和字段映射，包括 API 密钥、默认文件路径、以及 Form 8843 字段和 PDF 表单域的映射关系。

# OpenAI API Key，用于调用 GPT-4o 提取 W-2 表单字段，可替换
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 默认路径设置（PDF 路径、输出路径、JSON 存储等）默认路径设置（PDF 路径、输出路径、JSON 存储等）
DEFAULT_W2_PDF_PATH = "W2_sample.pdf"
DEFAULT_8843_TEMPLATE_PATH = "f8843_blank.pdf"
DEFAULT_OUTPUT_PDF_PATH = "filled_8843.pdf"
DEFAULT_FLATTENED_PDF_PATH = "filled_8843_flat.pdf"
DEFAULT_W2_DATA_JSON = "w2_data.json"

# 8843 表单逻辑字段（例如 first_name）到 PDF 表单字段名（如 f1_4[0]）的映射关系
# 用于自动填写 PDF 表单
form_8843_fields_map = {
    # Header Info
    "beginning date": "f1_1[0]",
    "ending date": "f1_2[0]",
    "ending year(last two number 20__)": "f1_3[0]",
    "first_name": "f1_4[0]",
    "last_name": "f1_5[0]",
    "TIN": "f1_6[0]",
    "Address in country of residence": "f1_7[0]",
    "Address in the United States": "f1_8[0]",

    # Part I - General Information
    "visa_type": "f1_9[0]",
    "Current nonimmigrant status": "f1_10[0]",
    "country of citizenship": "f1_11[0]",
    "passport_country": "f1_12[0]",
    "passport_number": "f1_13[0]",
    "days in USA_2024": "f1_14[0]",
    "days in USA_2023": "f1_15[0]",
    "days in USA_2022": "f1_16[0]",
    "exclude_days": "f1_17[0]",

    # Part II - Teachers and Trainees
    "teacher_name_2024": "f1_18[0]",
    "teacher_address_2024": "f1_19[0]",
    "teacher_phone_2024": "f1_20[0]",
    "trainee_director_name_2024": "f1_21[0]",
    "trainee_director_address_2024": "f1_22[0]",
    "trainee_director_phone_2024": "f1_23[0]",
    "visa_2018": "f1_24[0]",
    "visa_2019": "f1_25[0]",
    "visa_2020": "f1_26[0]",
    "visa_2021": "f1_27[0]",
    "visa_2022": "f1_28[0]",
    "visa_2023": "f1_29[0]",
    "exempt_as_teacher_or_trainee_yes": "c1_1[0]",
    "exempt_as_teacher_or_trainee_no": "c1_1[1]",

    # Part III - Students
    "school_name in 2024": "f1_30[0]",
    "school_phone in 2024": "f1_31[0]",
    "school_address in 2024": "f1_32[0]",
    "director_name in 2024": "f1_33[0]",
    "director_phone in 2024": "f1_34[0]",
    "director_address in 2024": "f1_35[0]",
    "type of U.S. visa (F, J, M, or Q) in 2018": "f1_36[0]",
    "type of U.S. visa (F, J, M, or Q) in 2019": "f1_37[0]",
    "type of U.S. visa (F, J, M, or Q) in 2020": "f1_38[0]",
    "type of U.S. visa (F, J, M, or Q) in 2021": "f1_39[0]",
    "type of U.S. visa (F, J, M, or Q) in 2022": "f1_40[0]",
    "type of U.S. visa (F, J, M, or Q) in 2023": "f1_41[0]",
    "exempt_as_student_yes": "c1_2[0]",
    "exempt_as_student_no": "c1_2[1]",
    "green_card_applied_yes": "c1_3[0]",
    "green_card_applied_no": "c1_3[1]",
    "green_card_explanation_1": "f1_42[0]",
    "green_card_explanation_2": "f1_43[0]",
    "green_card_explanation_3": "f1_44[0]",

    # Part IV - Professional Athletes
    "charitable_event_name_1": "f2_1[0]",
    "charitable_event_name_2": "f2_2[0]",
    "charitable_event_name_3": "f2_3[0]",
    "charitable_org_1": "f2_4[0]",
    "charitable_org_2": "f2_5[0]",
    "charitable_org_3": "f2_6[0]",

    # Part V - Medical Condition
    "medical_condition_line1": "f2_7[0]",
    "medical_condition_line2": "f2_8[0]",
    "medical_condition_line3": "f2_9[0]",
    "medical_condition_line4": "f2_10[0]",
    "intended_departure_date": "f2_11[0]",
    "actual_departure_date": "f2_12[0]",
    "physician_certify_name": "f2_13[0]",
    "physician_name": "f2_14[0]",
    "physician_address_and_phone": "f2_15[0]",
}
