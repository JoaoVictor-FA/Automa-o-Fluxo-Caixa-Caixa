from PyPDF2 import PdfReader

# Abrindo um arquivo PDF existente
with open("extrato.pdf", "rb") as input_pdf:
    # Criando um objeto PdfFileReader
    pdf_reader = PdfReader(input_pdf)

    # Obtendo o número de páginas do arquivo PDF
    num_pages = len(pdf_reader.pages)

    # Lendo o texto de cada página
    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        text = page.extract_text()
        print("Texto da página", page_number + 1, ":", text)
