import pdfplumber


def extract_po_details(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()

        price = extract_price(text)
        quantity = extract_quantity(text)
        date = extract_date(text)

        return price, quantity, date


def extract_price(text):
    # Implement price extraction logic
    pass


def extract_quantity(text):
    # Implement quantity extraction logic
    pass


def extract_date(text):
    # Implement date extraction logic
    pass
