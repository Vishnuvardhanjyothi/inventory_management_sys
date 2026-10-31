from database import con, cur


def view_customers():
    cur.execute("SELECT * FROM customers")

    data = cur.fetchall()

    for customer in data:
        print("ID:", customer[0])
        print("Name:", customer[1])
        print("Phone:", customer[2])
        print("Email:", customer[3])
        print("----------------")

def add_customer():
    customer_name = input("Enter customer name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    query = """
    INSERT INTO customers
    (customer_name, phone, email)
    VALUES (%s, %s, %s)
    """

    values = (customer_name, phone, email)

    cur.execute(query, values)

    con.commit()

    print("Customer added successfully")

