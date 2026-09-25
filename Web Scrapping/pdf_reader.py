import fitz

def read_pdf(file_path):
    doc = fitz.open(file_path)
    all_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        all_text += page.get_text()

    doc.close()
    return all_text

if __name__ == "__main__":
    file_path = "sample.pdf"
    try:
        content = read_pdf(file_path)
        print("*" * 20)
        print(content)
        print("*" * 20)
    except Exception as e:
        print(f"Error: {e}")