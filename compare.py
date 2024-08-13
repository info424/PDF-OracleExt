def compare_po_details(extracted_details, oracle_details):
    extracted_price, extracted_quantity, extracted_date = extracted_details
    oracle_price, oracle_quantity, oracle_date = oracle_details

    discrepancies = {
        "price": extracted_price != oracle_price,
        "quantity": extracted_quantity != oracle_quantity,
        "date": extracted_date != oracle_date,
    }

    return discrepancies
