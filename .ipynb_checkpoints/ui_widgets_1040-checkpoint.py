# 📄 ui_widgets_1040.py

# ============================
# 📄 UI Widgets for IRS Form 1040
# ============================
# 让用户在 Notebook 中输入姓名、收入、纳税情况等所有内容。后面用来显示在 Notebook UI 界面的输入框们。

import ipywidgets as widgets

# === 控件通用样式设置 ===
default_layout = widgets.Layout(width='600px')
default_style = {'description_width': 'initial'}

# === 表头区域信息 ===
beginning_date = widgets.Text(description="Tax Beginning Date", layout=default_layout, style=default_style)
ending_date = widgets.Text(description="Tax Ending Date", layout=default_layout, style=default_style)
ending_year = widgets.Text(description="Tax Ending Year (20__)", layout=default_layout, style=default_style)

# === 基本身份信息 ===
taxpayer_first_name = widgets.Text(description="Taxpayer's First Name and middle initial", layout=default_layout, style=default_style)
taxpayer_last_name = widgets.Text(description="Taxpayer's Last Name", layout=default_layout, style=default_style)
taxpayer_ssn = widgets.Text(description="Taxpayer's SSN", layout=default_layout, style=default_style)
spouse_first_name = widgets.Text(description="Spouse's First Name and middle initial", layout=default_layout, style=default_style)
spouse_last_name = widgets.Text(description="Spouse's Last Name", layout=default_layout, style=default_style)
spouse_ssn = widgets.Text(description="Spouse's SSN", layout=default_layout, style=default_style)

# === 居住地址 ===
home_address = widgets.Text(description="Home Address", layout=default_layout, style=default_style)
home_address_apt = widgets.Text(description="Apt. No.", layout=default_layout, style=default_style)
home_address_city = widgets.Text(description="City", layout=default_layout, style=default_style)
home_address_state = widgets.Text(description="State", layout=default_layout, style=default_style)
home_address_zip = widgets.Text(description="ZIP Code", layout=default_layout, style=default_style)
foreign_country = widgets.Text(description="Foreign Country", layout=default_layout, style=default_style)
foreign_state_province = widgets.Text(description="Foreign State/Province", layout=default_layout, style=default_style)
foreign_postal_code = widgets.Text(description="Foreign Postal Code", layout=default_layout, style=default_style)

# === Presidential Election Campaign ===
presidential_campaign_you = widgets.Checkbox(description="Presidential Campaign Fund - You", layout=default_layout, style=default_style)
presidential_campaign_spouse = widgets.Checkbox(description="Presidential Campaign Fund - Spouse", layout=default_layout, style=default_style)

# === Filing Status ===
filing_status = widgets.RadioButtons(
    options=[
        "Single",
        "Married filing jointly",
        "Married filing separately",
        "Head of household",
        "Qualifying surviving spouse"
    ],
    description="Filing Status",
    layout=default_layout,
    style=default_style
)

qualifying_person_name = widgets.Text(
    description="Spouse/Child Name (if MFS/HOH/QSS)", 
    placeholder="Enter spouse/child name if applicable", 
    layout=default_layout, style=default_style)


treat_nonresident_as_us = widgets.Checkbox(
    description="Treat nonresident/dual-status spouse as U.S. resident",
    layout=default_layout, style=default_style
)

nonresident_spouse_name = widgets.Text(
    description="Spouse Name (if treated as U.S. resident)",
    placeholder="Enter spouse name if checked above",
    layout=default_layout, style=default_style
)

# === Digital Assets ===
digital_assets = widgets.RadioButtons(
    options=["Yes", "No"],
    description="Did you receive, sell, exchange, or otherwise dispose of any digital asset?",
    layout=default_layout, style=default_style
)

# === Standard Deduction ===
you_as_dependent = widgets.Checkbox(description="You as a dependent",
                                    layout=default_layout, style=default_style)
spouse_as_dependent = widgets.Checkbox(description="Your spouse as a dependent",
                                       layout=default_layout, style=default_style)
spouse_itemizes = widgets.Checkbox(description="Spouse itemizes on a separate return or you were a dual-status alien",
                                   layout=default_layout, style=default_style)
you_born_before_1960_Jan_2 = widgets.Checkbox(description="You: Were born before January 2, 1960",
                                              layout=default_layout, style=default_style)
you_are_blind = widgets.Checkbox(description="You: Are blind",
                                 layout=default_layout, style=default_style)
spouse_born_before_1960_Jan_2 = widgets.Checkbox(description="Spouse: Was born before January 2, 1960",
                                                 layout=default_layout, style=default_style)
spouse_is_blind = widgets.Checkbox(description="Spouse: Is blind",
                                   layout=default_layout, style=default_style)

# === 受抚养人信息 ===
dependent1_name = widgets.Text(description="Dependent 1 Name",layout=default_layout, style=default_style)
dependent1_ssn = widgets.Text(description="Dependent 1 SSN",layout=default_layout, style=default_style)
dependent1_relationship = widgets.Text(description="Dependent 1 Relationship to you",layout=default_layout, style=default_style)
dependent1_child_tax_credit = widgets.Checkbox(description="Dependent 1: Child Tax Credit",layout=default_layout, style=default_style)
dependent1_other_credit = widgets.Checkbox(description="Dependent 1: Credit for other dependents",layout=default_layout, style=default_style)

dependent2_name = widgets.Text(description="Dependent 2 Name",layout=default_layout, style=default_style)
dependent2_ssn = widgets.Text(description="Dependent 2 SSN",layout=default_layout, style=default_style)
dependent2_relationship = widgets.Text(description="Dependent 2 Relationship to you",layout=default_layout, style=default_style)
dependent2_child_tax_credit = widgets.Checkbox(description="Dependent 2: Child Tax Credit",layout=default_layout, style=default_style)
dependent2_other_credit = widgets.Checkbox(description="Dependent 2: Credit for other dependents",layout=default_layout, style=default_style)

dependent3_name = widgets.Text(description="Dependent 3 Name",layout=default_layout, style=default_style)
dependent3_ssn = widgets.Text(description="Dependent 3 SSN",layout=default_layout, style=default_style)
dependent3_relationship = widgets.Text(description="Dependent 3 Relationship to you",layout=default_layout, style=default_style)
dependent3_child_tax_credit = widgets.Checkbox(description="Dependent 3: Child Tax Credit",layout=default_layout, style=default_style)
dependent3_other_credit = widgets.Checkbox(description="Dependent 3: Credit for other dependents",layout=default_layout, style=default_style)

dependent4_name = widgets.Text(description="Dependent 4 Name",layout=default_layout, style=default_style)
dependent4_ssn = widgets.Text(description="Dependent 4 SSN",layout=default_layout, style=default_style)
dependent4_relationship = widgets.Text(description="Dependent 4 Relationship to you",layout=default_layout, style=default_style)
dependent4_child_tax_credit = widgets.Checkbox(description="Dependent 4: Child Tax Credit",layout=default_layout, style=default_style)
dependent4_other_credit = widgets.Checkbox(description="Dependent 4: Credit for other dependents",layout=default_layout, style=default_style)

dependents_more_than_4 = widgets.Checkbox(description="More than 4 dependents?",layout=default_layout, style=default_style)


# === 收入信息（Income Section） ===
line_1a = widgets.FloatText(description="1a. Wages from W-2 (Box 1)", layout=default_layout, style=default_style)
line_1b = widgets.FloatText(description="1b. Household employee wages not on W-2", layout=default_layout, style=default_style)
line_1c = widgets.FloatText(description="1c. Tip income not on W-2", layout=default_layout, style=default_style)
line_1d = widgets.FloatText(description="1d. Medicaid waiver payments (not on W-2)", layout=default_layout, style=default_style)
line_1e = widgets.FloatText(description="1e. Taxable dependent care benefits (Form 2441, Line 26)", layout=default_layout, style=default_style)
line_1f = widgets.FloatText(description="1f. Adoption benefits (Form 8839, Line 29)", layout=default_layout, style=default_style)
line_1g = widgets.FloatText(description="1g. Wages from Form 8919, Line 6", layout=default_layout, style=default_style)
line_1h = widgets.FloatText(description="1h. Other earned income", layout=default_layout, style=default_style)
line_1i = widgets.FloatText(description="1i. Nontaxable combat pay election", layout=default_layout, style=default_style)
line_1z = widgets.FloatText(description="1z. Total earned income (1a–1h)", layout=default_layout, style=default_style)

line_2a = widgets.FloatText(description="2a. Tax-exempt interest", layout=default_layout, style=default_style)
line_2b = widgets.FloatText(description="2b. Taxable interest", layout=default_layout, style=default_style)

line_3a = widgets.FloatText(description="3a. Qualified dividends", layout=default_layout, style=default_style)
line_3b = widgets.FloatText(description="3b. Ordinary dividends", layout=default_layout, style=default_style)

line_4a = widgets.FloatText(description="4a. IRA distributions", layout=default_layout, style=default_style)
line_4b = widgets.FloatText(description="4b. Taxable amount (IRA)", layout=default_layout, style=default_style)

line_5a = widgets.FloatText(description="5a. Pensions and annuities", layout=default_layout, style=default_style)
line_5b = widgets.FloatText(description="5b. Taxable amount (pensions)", layout=default_layout, style=default_style)

line_6a = widgets.FloatText(description="6a. Social Security benefits", layout=default_layout, style=default_style)
line_6b = widgets.FloatText(description="6b. Taxable Social Security amount", layout=default_layout, style=default_style)
line_6c = widgets.Checkbox(description="6c. Lump-sum election (if applicable)", layout=default_layout, style=default_style)

line_7 = widgets.FloatText(description="7. Capital gain or loss", layout=default_layout, style=default_style)
line_7_schedule_d = widgets.Checkbox(description="Attach Schedule D?", layout=default_layout, style=default_style)

line_8 = widgets.FloatText(description="8. Additional income (Schedule 1, line 10)", layout=default_layout, style=default_style)
line_9 = widgets.FloatText(description="9. Total income (Add lines 1z, 2b, 3b, 4b, 5b, 6b, 7, and 8)", layout=default_layout, style=default_style)
line_10 = widgets.FloatText(description="10. Adjustments (Schedule 1, line 26)", layout=default_layout, style=default_style)
line_11 = widgets.FloatText(description="11. Adjusted gross income", layout=default_layout, style=default_style)
line_12 = widgets.FloatText(description="12. Standard/itemized deduction (Schedule A)", layout=default_layout, style=default_style)
line_13 = widgets.FloatText(description="13. QBI deduction (Form 8995 or 8995-A)", layout=default_layout, style=default_style)
line_14 = widgets.FloatText(description="14. Total of lines 12 and 13", layout=default_layout, style=default_style)
line_15 = widgets.FloatText(description="15. Taxable income (line 11 - line 14)", layout=default_layout, style=default_style)

# === 税额和抵免 Tax and Credits ===
line_16_form_8814 = widgets.Checkbox(description="From Form 8814", layout=default_layout, style=default_style)
line_16_form_4972 = widgets.Checkbox(description="From Form 4972", layout=default_layout, style=default_style)
line_16_other_form_check = widgets.Checkbox(description="From other form", layout=default_layout, style=default_style)
line_16_other_form_text = widgets.Text(description="Other Form (number)", layout=default_layout, style=default_style)
line_16_tax = widgets.FloatText(description="16. Tax", layout=default_layout, style=default_style)

line_17 = widgets.FloatText(description="17. Amount from Schedule 2, line 3", layout=default_layout, style=default_style)
line_18 = widgets.FloatText(description="18. Add lines 16 and 17", layout=default_layout, style=default_style)
line_19 = widgets.FloatText(description="19. Child tax credit or credit for other dependents", layout=default_layout, style=default_style)
line_20 = widgets.FloatText(description="20. Amount from Schedule 3, line 8", layout=default_layout, style=default_style)
line_21 = widgets.FloatText(description="21. Add lines 19 and 20", layout=default_layout, style=default_style)
line_22 = widgets.FloatText(description="22. Subtract line 21 from line 18. If zero or less, enter -0-", layout=default_layout, style=default_style)
line_23 = widgets.FloatText(description="23. Other taxes (e.g., self-employment tax) from Schedule 2, line 21", layout=default_layout, style=default_style)
line_24 = widgets.FloatText(description="24. Add lines 22 and 23. This is your total tax", layout=default_layout, style=default_style)

# ▶️ Payments Section (Line 25 to 32)
line_25a = widgets.FloatText(description="25a. Withheld from W-2", layout=default_layout, style=default_style)
line_25b = widgets.FloatText(description="25b. Withheld from 1099", layout=default_layout, style=default_style)
line_25c = widgets.FloatText(description="25c. Withheld from other forms", layout=default_layout, style=default_style)
line_25d = widgets.FloatText(description="25d. Total from 25a to 25c", layout=default_layout, style=default_style)

line_26 = widgets.FloatText(description="26. 2024 estimated tax payments and prior year credits", layout=default_layout, style=default_style)

line_27 = widgets.FloatText(description="27. Earned income credit (EIC)", layout=default_layout, style=default_style)
line_28 = widgets.FloatText(description="28. Additional child tax credit (Schedule 8812)", layout=default_layout, style=default_style)
line_29 = widgets.FloatText(description="29. American opportunity credit (Form 8863, line 8)", layout=default_layout, style=default_style)
line_30 = widgets.FloatText(description="30. Reserved for future use", layout=default_layout, style=default_style)
line_31 = widgets.FloatText(description="31. From Schedule 3, line 15", layout=default_layout, style=default_style)
line_32 = widgets.FloatText(description="32. Add lines 27–31: Other payments and refundable credits", layout=default_layout, style=default_style)

# === 退款和应付金额 ===
line_33 = widgets.FloatText(description="33. Total Payments", layout=default_layout, style=default_style)
line_34 = widgets.FloatText(description="34. Overpaid (if line 33 > line 24)", layout=default_layout, style=default_style)
line_35a = widgets.FloatText(description="35a. Amount you want refunded", layout=default_layout, style=default_style)
line_35b = widgets.Text(description="35b. Routing number", layout=default_layout, style=default_style)
line_35c = widgets.RadioButtons(
    options=["Checking", "Savings"],
    description="35c. Account Type:",
    layout=default_layout,
    style=default_style
)
line_35d = widgets.Text(description="35d. Account number", layout=default_layout, style=default_style)
line_36 = widgets.FloatText(description="36. Amount applied to 2025 estimated tax", layout=default_layout, style=default_style)

line_37 = widgets.FloatText(description="37. Amount you owe (line 24 - line 33)", layout=default_layout, style=default_style)
line_38 = widgets.FloatText(description="38. Estimated tax penalty", layout=default_layout, style=default_style)


# === 第三方指定人信息 ===
third_party_designee = widgets.RadioButtons(
    options=["Yes", "No"],
    description="Do you want to allow another person to discuss this return with the IRS?",
    layout=default_layout,
    style=default_style
)

yes_label = widgets.HTML("<b style='color:green'>✔ Yes. Complete below:</b>")

designee_name = widgets.Text(description="Designee's Name", layout=default_layout, style=default_style)
designee_phone = widgets.Text(description="Designee's Phone Number", layout=default_layout, style=default_style)
designee_pin = widgets.Text(description="Designee's PIN", layout=default_layout, style=default_style)

# 分组展示（默认隐藏）
designee_inputs = widgets.VBox([
    yes_label,
    widgets.HBox([designee_name, designee_phone, designee_pin])
])
designee_inputs.layout.display = "none"

# 控制逻辑函数
def toggle_designee_inputs(change):
    designee_inputs.layout.display = "block" if change["new"] == "Yes" else "none"

# 绑定逻辑
third_party_designee.observe(toggle_designee_inputs, names="value")


# === 签名信息 ===
your_occupation = widgets.Text(description="Your Occupation", layout=default_layout, style=default_style)
your_ip_pin = widgets.Text(description="Your IP PIN", layout=default_layout, style=default_style)
spouse_occupation = widgets.Text(description="Spouse's Occupation", layout=default_layout, style=default_style)
spouse_ip_pin = widgets.Text(description="Spouse's IP PIN", layout=default_layout, style=default_style)
phone_number = widgets.Text(description="Phone Number", layout=default_layout, style=default_style)
email_address = widgets.Text(description="Email Address", layout=default_layout, style=default_style)

# === 税务准备人信息 ===
preparer_name = widgets.Text(description="Preparer's Name", layout=default_layout, style=default_style)
preparer_ptin = widgets.Text(description="Preparer's PTIN", layout=default_layout, style=default_style)
preparer_self_employed = widgets.Checkbox(description="Self-employed", layout=default_layout, style=default_style)
firm_name = widgets.Text(description="Firm's Name", layout=default_layout, style=default_style)
firm_phone = widgets.Text(description="Firm's Phone Number", layout=default_layout, style=default_style)
firm_address = widgets.Text(description="Firm's Address", layout=default_layout, style=default_style)
firm_ein = widgets.Text(description="Firm's EIN", layout=default_layout, style=default_style)


# === 控制区控件（W-2 提取和生成 1040）===
w2_pdf_path = widgets.Text(
    description="📎 W-2 PDF Path",
    value="W2_sample.pdf",
    layout=default_layout,
    style=default_style
)

template_path = widgets.Text(
    description="📎 Form 1040 Template PDF Path",
    value="f1040_blank.pdf",
    layout=default_layout,
    style=default_style
)

output_path = widgets.Text(
    description="📤 Output PDF Path",
    value="filled_1040.pdf",
    layout=default_layout,
    style=default_style
)

gpt_button = widgets.Button(
    description="🧠 Extract W-2",
    button_style="info",
    layout=widgets.Layout(width="200px")
)

gpt_json_output = widgets.Textarea(
    description="GPT Extracted JSON",
    layout=widgets.Layout(width="95%", height="100px"),
    style={"description_width": "initial"}
)

generate_button = widgets.Button(
    description="📝 Generate Form 1040",
    button_style="success",
    layout=widgets.Layout(width="250px")
)

manual_input_1040_widgets = {
    # Header
    "tax beginning(_/_,2024)": beginning_date,
    "tax ending(_/_)": ending_date,
    "tax ending year(20__)": ending_year,

    # Identity
    "taxpayer_first_name": taxpayer_first_name,
    "taxpayer_last_name": taxpayer_last_name,
    "taxpayer_ssn": taxpayer_ssn,
    "spouse_first_name": spouse_first_name,
    "spouse_last_name": spouse_last_name,
    "spouse_ssn": spouse_ssn,

    # Address
    "home_address(number and street)": home_address,
    "home_address_apt": home_address_apt,
    "home_address_city": home_address_city,
    "home_address_state": home_address_state,
    "home_address_zip": home_address_zip,
    "foreign_country(If you have a foreign address)": foreign_country,
    "foreign_state_province(If you have a foreign address)": foreign_state_province,
    "foreign_postal_code(If you have a foreign address)": foreign_postal_code,

    # Presidential Campaign
    "presidential_campaign_you": presidential_campaign_you,
    "presidential_campaign_spouse": presidential_campaign_spouse,

    # Filing Status (radio shared)
    "filing_status": filing_status,
    "name of your spouse or child": qualifying_person_name,
    "Whether treating a nonresident alien or dual-status alien spouse as a U.S. resident for the entire tax year": treat_nonresident_as_us,
    "enter their name if check the box": nonresident_spouse_name,

    # Digital Assets
    "digital_assets": digital_assets,

    # Standard Deduction & Age/Blindness
    "You as a dependent": you_as_dependent,
    "Your spouse as a dependent": spouse_as_dependent,
    "Spouse itemizes on a separate return or you were a dual-status alien": spouse_itemizes,
    "You: Were born before January 2, 1960": you_born_before_1960_Jan_2,
    "You: Are blind": you_are_blind,
    "Spouse: Was born before January 2, 1960": spouse_born_before_1960_Jan_2,
    "Spouse: Is blind": spouse_is_blind,

    # Dependents
    "(1) Firstname and Lastname": dependent1_name,
    "(1) Social security number": dependent1_ssn,
    "(1) Relationship to you": dependent1_relationship,
    "(1) Check the box if qualifies for: Child tax credit": dependent1_child_tax_credit,
    "(1) Check the box if qualifies for: Credit for other dependents": dependent1_other_credit,
    "(2) Firstname and Lastname": dependent2_name,
    "(2) Social security number": dependent2_ssn,
    "(2) Relationship to you": dependent2_relationship,
    "(2) Check the box if qualifies for: Child tax credit": dependent2_child_tax_credit,
    "(2) Check the box if qualifies for: Credit for other dependents": dependent2_other_credit,
    "(3) Firstname and Lastname": dependent3_name,
    "(3) Social security number": dependent3_ssn,
    "(3) Relationship to you": dependent3_relationship,
    "(3) Check the box if qualifies for: Child tax credit": dependent3_child_tax_credit,
    "(3) Check the box if qualifies for: Credit for other dependents": dependent3_other_credit,
    "(4) Firstname and Lastname": dependent4_name,
    "(4) Social security number": dependent4_ssn,
    "(4) Relationship to you": dependent4_relationship,
    "(4) Check the box if qualifies for: Child tax credit": dependent4_child_tax_credit,
    "(4) Check the box if qualifies for: Credit for other dependents": dependent4_other_credit,
    "If more than four dependents, see instructions and check here": dependents_more_than_4,

    # Income Lines 1a–15
    "1a) Total amount from Form(s) W-2, w2_income_box1": line_1a,
    "1b) Household employee wages not reported on Form(s) W-2": line_1b,
    "1c) Tip income not reported on line 1a (see instructions)": line_1c,
    "1d) Medicaid waiver payments not reported on Form(s) W-2 (see instructions)": line_1d,
    "1e) Taxable dependent care benefits from Form 2441, line 26": line_1e,
    "1f) Employer-provided adoption benefits from Form 8839, line 29": line_1f,
    "1g) Wages from Form 8919, line 6": line_1g,
    "1h) Other earned income (see instructions)": line_1h,
    "1i) Nontaxable combat pay election (see instructions)": line_1i,
    "1z) Add lines 1a through 1h": line_1z,
    "2a Tax-exempt interest": line_2a,
    "2b Taxable interest": line_2b,
    "3a Qualified dividends": line_3a,
    "3b Ordinary dividends": line_3b,
    "4a IRA distributions": line_4a,
    "4b Taxable amount": line_4b,
    "5a Pensions and annuities": line_5a,
    "5b Taxable amount": line_5b,
    "6a Social security benefits": line_6a,
    "6b Taxable amount": line_6b,
    "6c If you elect to use the lump-sum election method, check here (see instructions)": line_6c,
    "7 Capital gain or (loss). Attach Schedule D if required. If not required, check here": line_7,
    "8 Additional income from Schedule 1, line 10": line_8,
    "9 Add lines 1z, 2b, 3b, 4b, 5b, 6b, 7, and 8. This is your total income": line_9,
    "10 Adjustments to income from Schedule 1, line 26": line_10,
    "11 Subtract line 10 from line 9. This is your adjusted gross income": line_11,
    "12 Standard deduction or itemized deductions (from Schedule A)": line_12,
    "13 Qualified business income deduction from Form 8995 or Form 8995-A": line_13,
    "14 Add lines 12 and 13": line_14,
    "15 Subtract line 14 from line 11. If zero or less, enter -0-. This is your taxable income": line_15,

    # Taxes and Credits
    "16 Tax. ": line_16_tax,
    "17 Amount from Schedule 2, line 3": line_17,
    "18 Add lines 16 and 17": line_18,
    "19 Child tax credit or credit for other dependents from Schedule 881": line_19,
    "20 Amount from Schedule 3, line 8": line_20,
    "21 Add lines 19 and 20": line_21,
    "22 Subtract line 21 from line 18. If zero or less, enter -0-": line_22,
    "23 Other taxes, including self-employment tax, from Schedule 2, line 21": line_23,
    "24 Add lines 22 and 23. This is your total tax": line_24,

    # Payments
    "25a Federal income tax withheld from: Form(s) W-2": line_25a,
    "25b Federal income tax withheld from: Form(s) 1099": line_25b,
    "25c Federal income tax withheld from: Other forms (see instructions)": line_25c,
    "25d Add lines 25a through 25c": line_25d,
    "26 2024 estimated tax payments and amount applied from 2023 return": line_26,
    "27 Earned income credit (EIC)": line_27,
    "28 Additional child tax credit from Schedule 8812": line_28,
    "29 American opportunity credit from Form 8863, line 8": line_29,
    "30 Reserved for future use": line_30,
    "31 Amount from Schedule 3, line 15": line_31,
    "32 Add lines 27, 28, 29, and 31. These are your total other payments and refundable credits": line_32,
    "33 Add lines 25d, 26, and 32. These are your total payments": line_33,

    # Refund & Owe
    "34 If line 33 is more than line 24, subtract line 24 from line 33. This is the amount you overpaid": line_34,
    "35a Amount of line 34 you want refunded to you": line_35a,
    "35b Routing number": line_35b,
    "35c Type_Checking": line_35c,
    "35c Type_Savings": line_35c,
    "36d Account number": line_35d,
    "36 Amount of line 34 you want applied to your 2025 estimated tax .": line_36,
    "37 Subtract line 33 from line 24. This is the amount you owe.": line_37,
    "38 Estimated tax penalty (see instructions)": line_38,

    # Third Party
    "Do you want to allow another person to discuss this return with the IRS?_yes": third_party_designee,
    "Do you want to allow another person to discuss this return with the IRS?_no": third_party_designee,
    "Designee‘s name": designee_name,
    "Designee’s Phone no.": designee_phone,
    "Designee’s Personal identification number (PIN)": designee_pin,

    # Signature
    "Your occupation": your_occupation,
    "If the IRS sent you an Identity Protection PIN, enter it here": your_ip_pin,
    "Spouse’s occupation": spouse_occupation,
    "If the IRS sent your spouse an Identity Protection PIN, enter it here": spouse_ip_pin,
    "Phone no.": phone_number,
    "Email address": email_address,

    # Paid Preparer
    "Preparer’s name": preparer_name,
    "PTIN": preparer_ptin,
    "Check if: Self-employed": preparer_self_employed,
    "Firm’s name": firm_name,
    "Firm's Phone no.": firm_phone,
    "Firm’s address": firm_address,
    "Firm’s EIN": firm_ein,
    
}


# === 自动计算逻辑函数 ===
def bind_auto_calculation(target_widget, source_widgets, calc_fn):
    def update(*_):
        try:
            values = [float(w.value) if isinstance(w.value, (int, float)) else 0.0 for w in source_widgets]
            target_widget.value = round(calc_fn(*values), 2)
        except Exception:
            target_widget.value = 0.0

    for w in source_widgets:
        w.observe(update, names="value")

    update()

# === IRS 逻辑绑定 ===
bind_auto_calculation(line_1z, [line_1a, line_1b, line_1c, line_1d, line_1e, line_1f, line_1g, line_1h], lambda *args: sum(args))
bind_auto_calculation(line_9, [line_1z, line_2b, line_3b, line_4b, line_5b, line_6b, line_7, line_8], lambda *args: sum(args))
bind_auto_calculation(line_11, [line_9, line_10], lambda a, b: a - b)
bind_auto_calculation(line_14, [line_12, line_13], lambda a, b: a + b)
bind_auto_calculation(line_15, [line_11, line_14], lambda a, b: max(0, a - b))
bind_auto_calculation(line_18, [line_16_tax, line_17], lambda a, b: a + b)
bind_auto_calculation(line_21, [line_19, line_20], lambda a, b: a + b)
bind_auto_calculation(line_22, [line_18, line_21], lambda a, b: max(0, a - b))
bind_auto_calculation(line_24, [line_22, line_23], lambda a, b: a + b)
bind_auto_calculation(line_25d, [line_25a, line_25b, line_25c], lambda *args: sum(args))
bind_auto_calculation(line_32, [line_27, line_28, line_29, line_30, line_31], lambda *args: sum(args))
bind_auto_calculation(line_33, [line_25d, line_26, line_32], lambda *args: sum(args))
bind_auto_calculation(line_34, [line_33, line_24], lambda a, b: max(0, a - b))

# 限制 line_35a 不超过 line_34
def cap_line_35a(change=None):
    try:
        entered = float(line_35a.value)
        allowed_max = float(line_34.value)
        line_35a.value = max(0.0, min(entered, allowed_max))
    except Exception:
        line_35a.value = 0.0

line_35a.observe(cap_line_35a, names="value")
line_34.observe(cap_line_35a, names="value")

# 计算 36 和 37
bind_auto_calculation(line_36, [line_34, line_35a], lambda a, b: max(0, a - b))
bind_auto_calculation(line_37, [line_24, line_33], lambda a, b: max(0, a - b))