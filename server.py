from flask import Flask, request, send_file
import weasyprint, io

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/pdf", methods=["POST"])
def pdf():
    html = request.json.get("html", "")
    if not html:
        return {"error": "html requis"}, 400
    pdf_bytes = weasyprint.HTML(string=html).write_pdf()
    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype="application/pdf",
        download_name="document.pdf"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
