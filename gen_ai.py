from PyPDF2 import PdfReader

def gen_ai(pdf_path, question):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    # Dummy AI logic: return the first 1000 characters
    return f"PDF Summary:\n{text[:1000]}"
