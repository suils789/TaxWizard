# TaxWizard

This project provides an easy-to-use interface to extract W-2 information using GPT-4o, manually or semi-automatically complete **IRS Form 8843** and **Form 1040**, and export finalized PDFs.


##  Installation

1. Clone this repository:

```bash
git clone git@github.com:suils789/TaxWizard.git
cd TaxWizard

##  Install required Python packages:

pip install -r requirements.txt

##  Configuration

Open constants.py.
Replace the placeholder OPENAI_API_KEY with your actual OpenAI API key:
OPENAI_API_KEY = "your-openai-api-key-here"

##  Usage
Open and run main.py.
In the UI:  
    pload your W-2 PDF and blank Form 8843 template.
    Click Extract W-2 to auto-fill basic fields.
    Manually complete any missing information.
    Click Generate 8843 to export the completed Form 8843 PDF.

The filled and flattened PDFs will be saved to your local machine automatically.

## Project Structure

#Shared Components
constants.py	       API keys, file paths, field mappings
w2_extractor.py	       Functions for W-2 image extraction using GPT
requirements.txt	   Python package requirements
README.md	           Project documentation

#Form 8843 Module
form_8843_filler.py	   PDF filling and flattening (Form 8843)
ui_widgets.py	       UI widgets for Form 8843
ui_layout.py	       Layout assembly for 8843
main.py	               Main app entry for 8843

#Form 1040 Module
form_1040_filler.py	   PDF filling and flattening (Form 1040)
ui_widgets_1040.py	   UI widgets for Form 1040
ui_layout_1040.py	   Layout assembly for 1040
main_1040.py	       Main app entry for 1040




### Requirements (package)
openai
ipywidgets
pdf2image
Pillow
pdfrw
PyMuPDF (fitz)

