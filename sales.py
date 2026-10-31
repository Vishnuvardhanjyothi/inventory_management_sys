from database import con, cur


def add_sale():
    customer_id = int(input("Enter customer ID: "))
    sale_date = input("Enter sale date (YYYY-MM-DD): ")

    # Check customer
    check_query = """
    SELECT customer_id
    FROM customers
    WHERE customer_id = %s
    """

    cur.execute(check_query, (customer_id,))

    data = cur.fetchone()

    if data is None:
        print("Customer not found")
        return

    query = """
    INSERT INTO sales
    (customer_id, sale_date, total_amount)
    VALUES (%s, %s, %s)
    """

    values = (customer_id, sale_date, 0)

    cur.execute(query, values)

    con.commit()

    print("Sale created successfully")


def view_sales():
    cur.execute("SELECT * FROM sales")

    data = cur.fetchall()

    for sale in data:
        print("Sale ID:", sale[0])
        print("Customer ID:", sale[1])
        print("Sale Date:", sale[2])
        print("Total Amount:", sale[3])
        print("----------------")

def add_sale_item():
    sale_id = int(input("Enter sale ID: "))
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))

    # Check quantity
    if quantity <= 0:
        print("Quantity must be greater than 0")
        return

    price = float(input("Enter selling price: "))

    # Check available stock
    check_query = """
    SELECT stock
    FROM products
    WHERE product_id = %s
    """

    cur.execute(check_query, (product_id,))

    data = cur.fetchone()

    if data is None:
        print("Product not found")
        return

    stock = data[0]

    if quantity > stock:
        print("Insufficient stock")
        print("Available stock:", stock)
        return

    # Calculate item total
    item_total = quantity * price

    # Add sale item
    query = """
    INSERT INTO sale_items
    (sale_id, product_id, quantity, price)
    VALUES (%s, %s, %s, %s)
    """

    values = (sale_id, product_id, quantity, price)

    cur.execute(query, values)

    # Decrease stock
    update_query = """
    UPDATE products
    SET stock = stock - %s
    WHERE product_id = %s
    """

    update_values = (quantity, product_id)

    cur.execute(update_query, update_values)

    # Update sale total
    total_query = """
    UPDATE sales
    SET total_amount = total_amount + %s
    WHERE sale_id = %s
    """

    total_values = (item_total, sale_id)

    cur.execute(total_query, total_values)

    con.commit()

    print("Sale item added successfully")
    print("Item Total:", item_total)


def view_sale_items():
    cur.execute("SELECT * FROM sale_items")

    data = cur.fetchall()

    for item in data:
        print("Sale Item ID:", item[0])
        print("Sale ID:", item[1])
        print("Product ID:", item[2])
        print("Quantity:", item[3])
        print("Price:", item[4])
        print("----------------")