from database import con, cur


def add_supplier():
    supplier_name = input("Enter supplier name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    query = """
    INSERT INTO suppliers
    (supplier_name, phone, email)
    VALUES (%s, %s, %s)
    """

    values = (supplier_name, phone, email)

    cur.execute(query, values)

    con.commit()

    print("Supplier added successfully")

def view_suppliers():
    cur.execute("SELECT * FROM suppliers")

    data = cur.fetchall()

    for supplier in data:
        print("ID:", supplier[0])
        print("Name:", supplier[1])
        print("Phone:", supplier[2])
        print("Email:", supplier[3])
        print("----------------")