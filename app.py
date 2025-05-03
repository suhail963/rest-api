from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import uuid

from converter import convert_pdf_to_markdown

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"success": True, "message": "Service is running."})

@app.route("/convert", methods=["POST"])
def convert():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file uploaded."}), 400

    file = request.files['file']
    if not file.filename.endswith('.pdf'):
        return jsonify({"success": False, "message": "Invalid file format. Please upload a PDF."}), 400

    unique_id = str(uuid.uuid4())
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{unique_id}_{filename}")
    file.save(file_path)

    try:
        md_file_path = convert_pdf_to_markdown(file_path)
        with open(md_file_path, 'r', encoding='utf-8') as f:
            markdown_text = f.read()

        return jsonify({
            "success": True,
            "markdown": markdown_text,
            "download_url": f"/download/{os.path.basename(md_file_path)}"
        })

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory(
        directory=".",
        path=filename,
        as_attachment=True,
        mimetype="text/markdown",
        download_name=filename
    )

if __name__ == "__main__":
    app.run(debug=True)
