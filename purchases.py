from database import con, cur


def add_purchase():
    supplier_id = int(input("Enter supplier ID: "))
    purchase_date = input("Enter purchase date (YYYY-MM-DD): ")

    # Check supplier
    check_query = """
    SELECT supplier_id
    FROM suppliers
    WHERE supplier_id = %s
    """

    cur.execute(check_query, (supplier_id,))

    data = cur.fetchone()

    if data is None:
        print("Supplier not found")
        return

    query = """
    INSERT INTO purchases
    (supplier_id, purchase_date, total_amount)
    VALUES (%s, %s, %s)
    """

    values = (supplier_id, purchase_date, 0)

    cur.execute(query, values)

    con.commit()

    print("Purchase created successfully")


def view_purchase():   
    cur.execute("SELECT * FROM purchases")

    data = cur.fetchall()

    for purchase in data:
        print("ID:", purchase[0])
        print("Supplier ID:", purchase[1])
        print("Purchase Date:", purchase[2])
        print("Total Amount:", purchase[3])
        print("----------------")

def add_purchase_item():
    purchase_id = int(input("Enter purchase ID: "))
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter purchase price: "))

    # Check quantity
    if quantity <= 0:
        print("Quantity must be greater than 0")
        return

    if price <= 0:
        print("Purchase price must be greater than 0")
        return

    # Check product
    check_query = """
    SELECT product_id
    FROM products
    WHERE product_id = %s
    """

    cur.execute(check_query, (product_id,))

    data = cur.fetchone()

    if data is None:
        print("Product not found")
        return

    # Check purchase
    check_purchase = """
    SELECT purchase_id
    FROM purchases
    WHERE purchase_id = %s
    """

    cur.execute(check_purchase, (purchase_id,))

    purchase_data = cur.fetchone()

    if purchase_data is None:
        print("Purchase not found")
        return

    # Calculate item total
    item_total = quantity * price

    # Add purchase item
    query = """
    INSERT INTO purchase_items
    (purchase_id, product_id, quantity, price)
    VALUES (%s, %s, %s, %s)
    """

    values = (purchase_id, product_id, quantity, price)

    cur.execute(query, values)

    # Increase stock
    update_query = """
    UPDATE products
    SET stock = stock + %s
    WHERE product_id = %s
    """

    update_values = (quantity, product_id)

    cur.execute(update_query, update_values)

    # Update purchase total
    total_query = """
    UPDATE purchases
    SET total_amount = total_amount + %s
    WHERE purchase_id = %s
    """

    total_values = (item_total, purchase_id)

    cur.execute(total_query, total_values)

    con.commit()

    print("Purchase item added successfully")
    print("Item Total:", item_total)

def view_purchase_items():
    cur.execute("SELECT * FROM purchase_items")

    data = cur.fetchall()

    for item in data:
        print("ID:", item[0])
        print("Purchase ID:", item[1])
        print("Product ID:", item[2])
        print("Quantity:", item[3])
        print("Price:", item[4])
        print("----------------")