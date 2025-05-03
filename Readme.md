
## PDF to Structured Markdown Converter (Flask API)

This project is a Flask-based backend that converts PDF files into clean, structured Markdown (`.md`) format. It handles both text-based and image-based (scanned) PDFs using OCR, and exposes the functionality via a REST API with a simple frontend.

---

## ✅ Features

 Extracts clean, readable text from PDFs  
 Supports OCR for scanned PDFs (Tesseract)  
 Preserves structure: headings, subheadings, bullet points  
 Outputs clean Markdown using standard syntax  
 Provides RESTful API (`/convert`, `/health`)  
 Includes a simple frontend for file uploads  

---

## 🧰 Tech Stack

 Python 3.8+  
 Flask (REST API framework)  
 pdfplumber (text extraction)  
 pytesseract (OCR for scanned text)  
 pdf2image (for converting PDF pages to images)  


---

##  Installation

# 1. Clone the Repository


git clone https://github.com/your-username/pdf-to-md-converter.git
cd pdf-to-md-converter
2. Create Virtual Environment (optional)

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install Python Dependencies

pip install -r requirements.txt
4. Install External Tools
Tesseract-OCR
Install from: https://github.com/tesseract-ocr/tesseract
Ensure tesseract is in your system path.

Used by pdf2image to convert PDFs to images.
Install:

Ubuntu: sudo apt install poppler-utils

Windows: https://blog.alivate.com.au/poppler-windows/

# Running the Application

python app.py
Visit: http://127.0.0.1:5000/

# API Endpoints
GET /health
Returns API status.

json

{
  "success": true,
  "message": "Service is running."
}
POST /convert
Uploads a PDF and returns the Markdown output.

Request:
Type: multipart/form-data

Field: file — the PDF file

Response (example):
json

{
  "success": true,
  "markdown": "## Introduction\n\n# - This is a bullet point\n\n## Conclusion"
}
# Testing with Postman
1. Use POST http://127.0.0.1:5000/convert
2. Set file as form-data and upload a PDF
3. Get Markdown in JSON response
📁 Project Structure

.
├── app.py             
├── converter.py       
├── templates/
│   └── index.html     
├── uploads/           
├── requirements.txt    
└── README.md
⚠️ Notes
Max upload size: 5MB
Markdown is returned via API; not saved to disk
Images are not embedded into .md file
Error handling returns JSON with descriptive messages