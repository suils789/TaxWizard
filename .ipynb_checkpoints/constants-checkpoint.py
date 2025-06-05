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
DEFAULT_1040_TEMPLATE_PATH = "f1040_blank.pdf"
DEFAULT_OUTPUT_PDF_PATH_1040 = "filled_1040.pdf"
DEFAULT_OUTPUT_FLATTENED_PDF_PATH_1040 = "filled_1040_flat.pdf"



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


# 📌 1040 字段映射
# 将逻辑字段（我们 UI 和数据中使用的名字）映射到 PDF 表单里的真实字段名（XFA 名称）。
form_1040_fields_map = {
    # Page 1 - Identity Information
    "tax beginning(_/_,2024)": "topmostSubform[0].Page1[0].f1_01[0]",
    "tax ending(_/_)": "topmostSubform[0].Page1[0].f1_02[0]",
    "tax ending year(20__)": "topmostSubform[0].Page1[0].f1_03[0]",
    "taxpayer_first_name": "topmostSubform[0].Page1[0].f1_04[0]",
    "taxpayer_last_name": "topmostSubform[0].Page1[0].f1_05[0]",
    "taxpayer_ssn": "topmostSubform[0].Page1[0].f1_06[0]",
    
    # If joint return,
    "spouse_first_name": "topmostSubform[0].Page1[0].f1_07[0]",
    "spouse_last_name": "topmostSubform[0].Page1[0].f1_08[0]",
    "spouse_ssn": "topmostSubform[0].Page1[0].f1_09[0]",
    "home_address(number and street)": "topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_10[0]",
    "home_address_apt": "topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_11[0]",
    "home_address_city": "topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_12[0]",
    "home_address_state": "topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_13[0]",
    "home_address_zip": "topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_14[0]",
    # If you have a foreign address,please complete below
    "foreign_country(If you have a foreign address)": "topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_15[0]",
    "foreign_state_province(If you have a foreign address)": "topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_16[0]",
    "foreign_postal_code(If you have a foreign address)": "topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_17[0]",

    # Presidential Election Campaign
    # Check here if you, or your spouse if filing jointly, want $3 to go to this fund. Checking a box below will not change your tax or refund.
    "presidential_campaign_you": "topmostSubform[0].Page1[0].c1_1[0]",
    "presidential_campaign_spouse": "topmostSubform[0].Page1[0].c1_2[0]",

    # Filing status checkboxes (single, MFJ, MFS, HOH, QSS)
    "filing_status_Single": "topmostSubform[0].Page1[0].FilingStatus_ReadOrder[0].c1_3[0]",
    "filing_status_Married filing jointly (even if only one had income)": "topmostSubform[0].Page1[0].FilingStatus_ReadOrder[0].c1_3[1]",
    "filing_status_Married filing separately": "topmostSubform[0].Page1[0].FilingStatus_ReadOrder[0].c1_3[2]",
    "filing_status_Head of household": "topmostSubform[0].Page1[0].c1_3[0]",
    "filing_status_Qualifying surviving spouse": "topmostSubform[0].Page1[0].c1_3[1]",

    # If you checked the MFS box, enter the name of your spouse. If you checked the HOH or QSS box, enter the child’s name if the qualifying person is a child but not your dependent:
    "name of your spouse or child": "topmostSubform[0].Page1[0].f1_18[0]",
    # If treating a nonresident alien or dual-status alien spouse as a U.S. resident for the entire tax year, check the box and enter their name (see instructions and attach statement if required):
    "Whether treating a nonresident alien or dual-status alien spouse as a U.S. resident for the entire tax year": " topmostSubform[0].Page1[0].c1_4[0]",
    "enter their name if check the box": "topmostSubform[0].Page1[0].f1_19[0]",

    # Digital assets (yes/no)
    "digital_assets_yes": "topmostSubform[0].Page1[0].c1_5[0]",
    "digital_assets_no": "topmostSubform[0].Page1[0].c1_5[1]",

    # Standard Deduction
    "You as a dependent": "topmostSubform[0].Page1[0].c1_6[0]",
    "Your spouse as a dependent": "topmostSubform[0].Page1[0].c1_7[0]",
    "Spouse itemizes on a separate return or you were a dual-status alien": "topmostSubform[0].Page1[0].c1_8[0]",
    ###Age/Blindness
    "You: Were born before January 2, 1960": "topmostSubform[0].Page1[0].c1_9[0]",
    "You: Are blind": "topmostSubform[0].Page1[0].c1_10[0]",
    "Spouse: Was born before January 2, 1960": "topmostSubform[0].Page1[0].c1_11[0]",
    "Spouse: Is blind": "topmostSubform[0].Page1[0].c1_12[0]",

    #Dependents
    "If more than four dependents, see instructions and check here": "topmostSubform[0].Page1[0].Dependents_ReadOrder[0].c1_13[0]",
    "(1) Firstname and Lastname": "topmostSubform[0].Page1[0].Table_Dependents[0].Row1[0].f1_20[0]",
    "(1) Social security number": "topmostSubform[0].Page1[0].Table_Dependents[0].Row1[0].f1_21[0]",
    "(1) Relationship to you": "topmostSubform[0].Page1[0].Table_Dependents[0].Row1[0].f1_22[0]",
    "(1) Check the box if qualifies for: Child tax credit": "topmostSubform[0].Page1[0].Table_Dependents[0].Row1[0].c1_14[0]",
    "(1) Check the box if qualifies for: Credit for other dependents": "topmostSubform[0].Page1[0].Table_Dependents[0].Row1[0].c1_15[0]",
    "(2) Firstname and Lastname": "topmostSubform[0].Page1[0].Table_Dependents[0].Row2[0].f1_23[0]",
    "(2) Social security number": "topmostSubform[0].Page1[0].Table_Dependents[0].Row2[0].f1_24[0]",
    "(2) Relationship to you": "topmostSubform[0].Page1[0].Table_Dependents[0].Row2[0].f1_25[0]",
    "(2) Check the box if qualifies for: Child tax credit": "topmostSubform[0].Page1[0].Table_Dependents[0].Row2[0].c1_16[0]",
    "(2) Check the box if qualifies for: Credit for other dependents": "topmostSubform[0].Page1[0].Table_Dependents[0].Row2[0].c1_17[0]",
    "(3) Firstname and Lastname": "topmostSubform[0].Page1[0].Table_Dependents[0].Row3[0].f1_26[0]",
    "(3) Social security number": "topmostSubform[0].Page1[0].Table_Dependents[0].Row3[0].f1_27[0]",
    "(3) Relationship to you": "topmostSubform[0].Page1[0].Table_Dependents[0].Row3[0].f1_28[0]",
    "(3) Check the box if qualifies for: Child tax credit": "topmostSubform[0].Page1[0].Table_Dependents[0].Row3[0].c1_18[0]",
    "(3) Check the box if qualifies for: Credit for other dependents": "topmostSubform[0].Page1[0].Table_Dependents[0].Row3[0].c1_19[0]",
    "(4) Firstname and Lastname": "topmostSubform[0].Page1[0].Table_Dependents[0].Row4[0].f1_29[0]",
    "(4) Social security number": "topmostSubform[0].Page1[0].Table_Dependents[0].Row4[0].f1_30[0]",
    "(4) Relationship to you": "topmostSubform[0].Page1[0].Table_Dependents[0].Row4[0].f1_31[0]",
    "(4) Check the box if qualifies for: Child tax credit": "topmostSubform[0].Page1[0].Table_Dependents[0].Row4[0].c1_20[0]",
    "(4) Check the box if qualifies for: Credit for other dependents": "topmostSubform[0].Page1[0].Table_Dependents[0].Row4[0].c1_21[0]",

    # Income Section
    "1a) Total amount from Form(s) W-2, w2_income_box1": "topmostSubform[0].Page1[0].f1_32[0]",
    "1b) Household employee wages not reported on Form(s) W-2": "topmostSubform[0].Page1[0].f1_33[0]",
    "1c) Tip income not reported on line 1a (see instructions)": "topmostSubform[0].Page1[0].f1_34[0]",
    "1d) Medicaid waiver payments not reported on Form(s) W-2 (see instructions)": "topmostSubform[0].Page1[0].f1_35[0]",
    "1e) Taxable dependent care benefits from Form 2441, line 26": "topmostSubform[0].Page1[0].f1_36[0]",
    "1f) Employer-provided adoption benefits from Form 8839, line 29": "topmostSubform[0].Page1[0].f1_37[0]",
    "1g) Wages from Form 8919, line 6": "topmostSubform[0].Page1[0].f1_38[0]",
    "1h) Other earned income (see instructions)": "topmostSubform[0].Page1[0].f1_39[0]",
    "1i) Nontaxable combat pay election (see instructions)": "topmostSubform[0].Page1[0].f1_40[0]",
    "1z) Add lines 1a through 1h": "topmostSubform[0].Page1[0].f1_41[0]",

    "2a Tax-exempt interest": "topmostSubform[0].Page1[0].f1_42[0]",
    "2b Taxable interest": "topmostSubform[0].Page1[0].f1_43[0]",
    "3a Qualified dividends": "topmostSubform[0].Page1[0].f1_44[0]",
    "3b Ordinary dividends": "topmostSubform[0].Page1[0].f1_45[0]",
    "4a IRA distributions": "topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_46[0]",
    "4b Taxable amount": "topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_47[0]",
    "5a Pensions and annuities": "topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_48[0]",
    "5b Taxable amount":"topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_49[0]",
    "6a Social security benefits":"topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_50[0]",
    "6b Taxable amount":"topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_51[0]",
    "6c If you elect to use the lump-sum election method, check here (see instructions)": "topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].c1_22[0]",
    "7 Capital gain or (loss). Attach Schedule D if required. If not required, check here": "topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].c1_23[0]",
    "7 Capital gain or (loss)." : "topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_52[0]",
    "8 Additional income from Schedule 1, line 10": "topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_53[0]",
    "9 Add lines 1z, 2b, 3b, 4b, 5b, 6b, 7, and 8. This is your total income": "topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_54[0]",
    "10 Adjustments to income from Schedule 1, line 26": "topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_55[0]",
    "11 Subtract line 10 from line 9. This is your adjusted gross income": "topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_56[0]",
    "12 Standard deduction or itemized deductions (from Schedule A)": "topmostSubform[0].Page1[0].f1_57[0]",
    "13 Qualified business income deduction from Form 8995 or Form 8995-A": "topmostSubform[0].Page1[0].f1_58[0]",
    "14 Add lines 12 and 13": "topmostSubform[0].Page1[0].f1_59[0]",
    "15 Subtract line 14 from line 11. If zero or less, enter -0-. This is your taxable income": "topmostSubform[0].Page1[0].f1_60[0]",

    # Taxes & Credits
    "16 Tax. Check if from Form 8814:": "topmostSubform[0].Page2[0].c2_1[0]",
    "16 Tax. Check if from Form 4972:": "topmostSubform[0].Page2[0].c2_2[0]",
    "16 Tax. Check if from Form ____:": "topmostSubform[0].Page2[0].c2_3[0]",
    "16 Tax. Check if from Form ____:": "topmostSubform[0].Page2[0].f2_01[0]",
    "16 Tax. ": "topmostSubform[0].Page2[0].f2_02[0]",
    "17 Amount from Schedule 2, line 3": "topmostSubform[0].Page2[0].f2_03[0]",
    "18 Add lines 16 and 17": "topmostSubform[0].Page2[0].f2_04[0]",
    "19 Child tax credit or credit for other dependents from Schedule 881": "topmostSubform[0].Page2[0].f2_05[0]",
    "20 Amount from Schedule 3, line 8": "topmostSubform[0].Page2[0].f2_06[0]",
    "21 Add lines 19 and 20": "topmostSubform[0].Page2[0].f2_07[0]",
    "22 Subtract line 21 from line 18. If zero or less, enter -0-": "topmostSubform[0].Page2[0].f2_08[0]",
    "23 Other taxes, including self-employment tax, from Schedule 2, line 21": "topmostSubform[0].Page2[0].f2_09[0]",
    "24 Add lines 22 and 23. This is your total tax": "topmostSubform[0].Page2[0].f2_10[0]",

    # Payments
    "25a Federal income tax withheld from: Form(s) W-2": "topmostSubform[0].Page2[0].f2_11[0]",
    "25b Federal income tax withheld from: Form(s) 1099": "topmostSubform[0].Page2[0].f2_12[0]",
    "25c Federal income tax withheld from: Other forms (see instructions)": "topmostSubform[0].Page2[0].f2_13[0]",
    "25d Add lines 25a through 25c": "topmostSubform[0].Page2[0].f2_14[0]",
    "26 2024 estimated tax payments and amount applied from 2023 return": "topmostSubform[0].Page2[0].f2_15[0]",
    "27 Earned income credit (EIC)": "topmostSubform[0].Page2[0].f2_16[0]",
    "28 Additional child tax credit from Schedule 8812": "topmostSubform[0].Page2[0].f2_17[0]",
    "29 American opportunity credit from Form 8863, line 8": "topmostSubform[0].Page2[0].f2_18[0]",
    "30 Reserved for future use": "topmostSubform[0].Page2[0].f2_19[0]",
    "31 Amount from Schedule 3, line 15": "topmostSubform[0].Page2[0].f2_20[0]",
    "32 Add lines 27, 28, 29, and 31. These are your total other payments and refundable credits": "topmostSubform[0].Page2[0].f2_21[0]",
    "33 Add lines 25d, 26, and 32. These are your total payments": "topmostSubform[0].Page2[0].f2_22[0]",

    # Refund
    "34 If line 33 is more than line 24, subtract line 24 from line 33. This is the amount you overpaid": "topmostSubform[0].Page2[0].f2_23[0]",
    "35a Amount of line 34 you want refunded to you. If Form 8888 is attached, check here": "topmostSubform[0].Page2[0].c2_4[0]",
    "35a Amount of line 34 you want refunded to you": "topmostSubform[0].Page2[0].f2_24[0]",
    "35b Routing number": "topmostSubform[0].Page2[0].RoutingNo[0].f2_25[0]",
    "35c Type_Checking": "topmostSubform[0].Page2[0].c2_5[0]",
    "35c Type_Savings": "topmostSubform[0].Page2[0].c2_5[1]",
    "36d Account number": "topmostSubform[0].Page2[0].f2_26[0]",
    "36 Amount of line 34 you want applied to your 2025 estimated tax .": "topmostSubform[0].Page2[0].f2_27[0]",

    # Amount You Owe
    "37 Subtract line 33 from line 24. This is the amount you owe.": "topmostSubform[0].Page2[0].f2_28[0]",
    "38 Estimated tax penalty (see instructions)": "topmostSubform[0].Page2[0].f2_29[0]",

    # Third Party Designee
    "Do you want to allow another person to discuss this return with the IRS?_yes": "topmostSubform[0].Page2[0].c2_6[0]",
    "Do you want to allow another person to discuss this return with the IRS?_no": "topmostSubform[0].Page2[0].c2_6[1]",
    "Designee’s name": "topmostSubform[0].Page2[0].f2_30[0]",
    "Designee’s Phone no.": "topmostSubform[0].Page2[0].f2_31[0]",
    "Designee’s Personal identification number (PIN)": "topmostSubform[0].Page2[0].f2_32[0]",

    # Sign Here
    "Your occupation": "topmostSubform[0].Page2[0].f2_33[0]",
    "If the IRS sent you an Identity Protection PIN, enter it here": "topmostSubform[0].Page2[0].f2_34[0]",
    "Spouse’s occupation": "topmostSubform[0].Page2[0].f2_35[0]",
    "If the IRS sent your spouse an Identity Protection PIN, enter it here": "topmostSubform[0].Page2[0].f2_36[0]",
    "Phone no.": "topmostSubform[0].Page2[0].f2_37[0]",
    "Email address": "topmostSubform[0].Page2[0].f2_38[0]",

    # Paid Preparer Use Only
    "Preparer’s name": "topmostSubform[0].Page2[0].f2_39[0]",
    "PTIN": "topmostSubform[0].Page2[0].f2_40[0]",
    "Check if: Self-employed": "topmostSubform[0].Page2[0].c2_7[0]",
    "Firm’s name": "topmostSubform[0].Page2[0].f2_41[0]",
    "Firm's Phone no.": "topmostSubform[0].Page2[0].f2_42[0]",
    "Firm’s address": "topmostSubform[0].Page2[0].f2_43[0]",
    "Firm’s EIN": "topmostSubform[0].Page2[0].f2_44[0]",
    
}
