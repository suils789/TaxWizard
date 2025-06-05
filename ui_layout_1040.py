# ===============================
# 🧾 IRS Form 1040 - UI Layout
# ===============================
# 该文件组织并展示 ui_widgets_1040 中定义的所有控件，分区清晰，结构化排布

import ipywidgets as widgets
import ui_widgets_1040 as ui_1040

# 标题样式
def section_title(text):
    return widgets.HTML(value=f"<h4 style='color:navy'>{text}</h4>")

# 各分区控件
header_section = widgets.VBox([
    section_title("📄 Header Info"),
    ui_1040.beginning_date, ui_1040.ending_date, ui_1040.ending_year
])

identity_section = widgets.VBox([
    section_title("👤 Basic Identity Information"),
    ui_1040.taxpayer_first_name, ui_1040.taxpayer_last_name, ui_1040.taxpayer_ssn,
    ui_1040.spouse_first_name, ui_1040.spouse_last_name, ui_1040.spouse_ssn
])

address_section = widgets.VBox([
    section_title("📍 Address Information"),
    ui_1040.home_address, ui_1040.home_address_apt, ui_1040.home_address_city,
    ui_1040.home_address_state, ui_1040.home_address_zip,
    ui_1040.foreign_country, ui_1040.foreign_state_province, ui_1040.foreign_postal_code
])

presidential_campaign_section = widgets.VBox([
    section_title("🏛️ Presidential Election Campaign"),
    ui_1040.presidential_campaign_you, ui_1040.presidential_campaign_spouse
])

filing_status_section = widgets.VBox([
    section_title("📑 Filing Status"),
    ui_1040.filing_status,
    ui_1040.qualifying_person_name,
    ui_1040.treat_nonresident_as_us,
    ui_1040.nonresident_spouse_name
])

digital_assets_section = widgets.VBox([
    section_title("💻 Digital Assets"),
    ui_1040.digital_assets
])

standard_deduction_section = widgets.VBox([
    section_title("📉 Standard Deduction & Blindness / Age"),
    ui_1040.you_as_dependent, ui_1040.spouse_as_dependent, ui_1040.spouse_itemizes,
    ui_1040.you_born_before_1960_Jan_2, ui_1040.you_are_blind,
    ui_1040.spouse_born_before_1960_Jan_2, ui_1040.spouse_is_blind
])

dependents_section = widgets.VBox([
    section_title("👶 Dependents"),
    ui_1040.dependent1_name, ui_1040.dependent1_ssn, ui_1040.dependent1_relationship,
    ui_1040.dependent1_child_tax_credit, ui_1040.dependent1_other_credit,
    ui_1040.dependent2_name, ui_1040.dependent2_ssn, ui_1040.dependent2_relationship,
    ui_1040.dependent2_child_tax_credit, ui_1040.dependent2_other_credit,
    ui_1040.dependent3_name, ui_1040.dependent3_ssn, ui_1040.dependent3_relationship,
    ui_1040.dependent3_child_tax_credit, ui_1040.dependent3_other_credit,
    ui_1040.dependent4_name, ui_1040.dependent4_ssn, ui_1040.dependent4_relationship,
    ui_1040.dependent4_child_tax_credit, ui_1040.dependent4_other_credit,
    ui_1040.dependents_more_than_4
])

income_section = widgets.VBox([
    section_title("💰 Income"),
    ui_1040.line_1a, ui_1040.line_1b, ui_1040.line_1c, ui_1040.line_1d, ui_1040.line_1e,
    ui_1040.line_1f, ui_1040.line_1g, ui_1040.line_1h, ui_1040.line_1i, ui_1040.line_1z,
    ui_1040.line_2a, ui_1040.line_2b,
    ui_1040.line_3a, ui_1040.line_3b,
    ui_1040.line_4a, ui_1040.line_4b,
    ui_1040.line_5a, ui_1040.line_5b,
    ui_1040.line_6a, ui_1040.line_6b, ui_1040.line_6c,
    ui_1040.line_7, ui_1040.line_7_schedule_d,
    ui_1040.line_8, ui_1040.line_9, ui_1040.line_10,
    ui_1040.line_11, ui_1040.line_12, ui_1040.line_13,
    ui_1040.line_14, ui_1040.line_15
])

taxes_section = widgets.VBox([
    section_title("📌 Taxes and Credits"),
    widgets.Label("Line 16: Tax (Check if from the following forms)"),
    widgets.HBox([ui_1040.line_16_form_8814, ui_1040.line_16_form_4972, ui_1040.line_16_other_form_check]),
    ui_1040.line_16_other_form_text, ui_1040.line_16_tax,
    ui_1040.line_17, ui_1040.line_18, ui_1040.line_19, ui_1040.line_20, ui_1040.line_21,
    ui_1040.line_22, ui_1040.line_23, ui_1040.line_24
])

payments_section = widgets.VBox([
    section_title("💵 Payments"),
    ui_1040.line_25a, ui_1040.line_25b, ui_1040.line_25c, ui_1040.line_25d,
    ui_1040.line_26, ui_1040.line_27, ui_1040.line_28, ui_1040.line_29,
    ui_1040.line_30, ui_1040.line_31, ui_1040.line_32
])

refund_and_owe_section = widgets.VBox([
    section_title("💸 Refund and Amount You Owe"),
    ui_1040.line_33, ui_1040.line_34, ui_1040.line_35a,
    ui_1040.line_35b, ui_1040.line_35c, ui_1040.line_35d,
    ui_1040.line_36, ui_1040.line_37, ui_1040.line_38
])

third_party_section = widgets.VBox([
    section_title("📝 Third Party Designee"),
    ui_1040.third_party_designee,
    ui_1040.designee_inputs
])

signature_section = widgets.VBox([
    section_title("✍️ Sign Here"),
    ui_1040.your_occupation, ui_1040.your_ip_pin,
    ui_1040.spouse_occupation, ui_1040.spouse_ip_pin,
    ui_1040.phone_number, ui_1040.email_address
])

preparer_section = widgets.VBox([
    section_title("👔 Paid Preparer Use Only"),
    ui_1040.preparer_name, ui_1040.preparer_ptin, ui_1040.preparer_self_employed,
    ui_1040.firm_name, ui_1040.firm_phone, ui_1040.firm_address, ui_1040.firm_ein
])

control_section = widgets.VBox([
    section_title("🧠 W-2 GPT Extraction & Submit 1040"),
    ui_1040.w2_pdf_path,
    ui_1040.template_path,
    ui_1040.output_path,
    ui_1040.gpt_button,
    ui_1040.gpt_json_output,
    ui_1040.generate_button
])

# 🔚 主入口：导出 layout_1040 给 main_1040.py 使用
layout_1040 = widgets.VBox([
    header_section,
    identity_section,
    address_section,
    presidential_campaign_section,
    filing_status_section,
    digital_assets_section,
    standard_deduction_section,
    dependents_section,
    income_section,
    taxes_section,
    payments_section,
    refund_and_owe_section,
    third_party_section,
    signature_section,
    preparer_section,
    control_section
])
