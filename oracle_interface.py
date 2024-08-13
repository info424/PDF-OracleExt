import cx_Oracle


def get_po_details_from_oracle(po_number):
    dsn_tns = cx_Oracle.makedsn('host', 'port', service_name='service_name')
    conn = cx_Oracle.connect(user='username', password='password', dsn=dsn_tns)

    cursor = conn.cursor()
    query = "SELECT price, quantity, date FROM purchase_orders WHERE po_number = :po_number"
    cursor.execute(query, po_number=po_number)

    row = cursor.fetchone()
    cursor.close()
    conn.close()

    return row  # (price, quantity, date)
