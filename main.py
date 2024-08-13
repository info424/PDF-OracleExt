from pdf_extractor import extract_po_details
from oracle_interface import get_po_details_from_oracle
from compare import compare_po_details


def main(pdf_path, po_number):
    extracted_details = extract_po_details(pdf_path)
    oracle_details = get_po_details_from_oracle(po_number)

    discrepancies = compare_po_details(extracted_details, oracle_details)

    if any(discrepancies.values()):
        print("Discrepancies found:", discrepancies)
    else:
        print("All details match the Oracle records.")


if __name__ == "__main__":
    pdf_path = "path/to/po.pdf"
    po_number = "PO123456"
    main(pdf_path, po_number)
