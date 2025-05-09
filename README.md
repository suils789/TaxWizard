# TaxWizard

# 8843 Auto Generator

This project provides an easy-to-use interface to extract W-2 information using GPT-4o, manually edit Form 8843 fields, and generate completed 8843 PDF forms.

---

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
constants.py	       API keys, file paths, field mappings
w2_extractor.py	       Functions for W-2 image extraction using GPT
form_8843_filler.py	   PDF filling and flattening functions
ui_widgets.py	       UI input widgets
ui_layout.py	       Assemble the UI layout
main.py	               Main workflow
requirements.txt	   Python package requirements
README.md	           Project documentation

### Requirements (package)
openai
ipywidgets
pdf2image
Pillow
pdfrw
PyMuPDF (fitz)

