import re
from PyPDF2 import PdfFileReader

def extract_urls_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as f:
        pdf = PdfFileReader(f)
        urls = []
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)
            page_content = page.extractText()
            page_urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', page_content)
            urls.extend(page_urls)
        return urls

def main():
    pdf_file = "sample.pdf"
    urls = extract_urls_from_pdf(pdf_file)
    with open("output.txt", "w") as f:
        for url in urls:
            f.write(url + "\n")

if __name__ == "__main__":
    main()
