import pdfplumber
import pytesseract
from pdf2image import convert_from_path
import os
import re
import uuid

# Optional: Adjust path to tesseract if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def clean_text(text):
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        line = line.strip()
        if re.match(r'^\d+$', line):  # Remove page numbers
            continue
        if len(line) < 3:
            continue
        cleaned.append(line)
    return '\n'.join(cleaned)

def convert_text_to_markdown(text):
    markdown = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        # Heading detection: short, title-cased lines
        if line == line.title() and len(line.split()) <= 6:
            markdown.append(f"## {line}")
        # Bullet detection
        elif re.match(r'^[\-\*\•\▪]\s+', line):
            markdown.append(f"- {line[1:].strip()}")
        else:
            markdown.append(line)
    return '\n'.join(markdown)

def ocr_page(pdf_path, page_number):
    images = convert_from_path(pdf_path, first_page=page_number + 1, last_page=page_number + 1)
    return pytesseract.image_to_string(images[0])

def convert_pdf_to_markdown(pdf_path):
    unique_id = str(uuid.uuid4())
    output_md = f"output_{unique_id}.md"

    all_markdown = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                text = ocr_page(pdf_path, i)
            else:
                text = clean_text(text)
            md = convert_text_to_markdown(text)
            all_markdown.append(md)

    markdown_text = '\n\n'.join(all_markdown)
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(markdown_text)

    return output_md
