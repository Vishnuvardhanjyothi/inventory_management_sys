from database import con, cur

def view_products():
    cur.execute("SELECT * FROM products")

    data = cur.fetchall()

    for product in data:
        print("ID:", product[0])
        print("Name:", product[1])
        print("Price:", product[3])
        print("Stock:", product[4])
        print("----------------")



def add_product():
    product_name = input("Enter product name: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))

    if price <= 0:
        print("Price must be greater than 0")
        return

    if stock < 0:
        print("Stock cannot be negative")
        return

    query = """
    INSERT INTO products
    (product_name, category, price, stock)
    VALUES (%s, %s, %s, %s)
    """

    values = (product_name, category, price, stock)

    cur.execute(query, values)

    con.commit()

    print("Product added successfully")


