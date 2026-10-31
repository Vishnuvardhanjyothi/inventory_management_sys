from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
app = Flask(__name__)
CORS(app)

def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="VISHnu@2004",
        database="inventory_management"
    )
@app.route("/")
def home():
    return "Inventory Management API is running"


@app.route("/products")
def get_products():

    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        SELECT product_id, product_name, category, price, stock
        FROM products
    """)

    products = cur.fetchall()

    product_list = []

    for product in products:

        product_list.append({
            "product_id": product[0],
            "product_name": product[1],
            "category": product[2],
            "price": float(product[3]),
            "stock": product[4]
        })

    cur.close()
    con.close()

    return jsonify(product_list)


@app.route("/products/add", methods=["POST"])
def add_product_api():

    data = request.get_json()

    con = get_connection()
    cur = con.cursor()

    query = """
    INSERT INTO products
    (product_name, category, price, stock)
    VALUES (%s, %s, %s, %s)
    """

    cur.execute(
        query,
        (
            data["product_name"],
            data["category"],
            data["price"],
            data["stock"]
        )
    )

    con.commit()

    cur.close()
    con.close()

    return jsonify({
        "message": "Product added successfully"
    })


@app.route("/products/update/<int:product_id>", methods=["PUT"])
def update_product(product_id):

    data = request.get_json()

    con = get_connection()
    cur = con.cursor()

    query = """
    UPDATE products
    SET product_name = %s,
        category = %s,
        price = %s,
        stock = %s
    WHERE product_id = %s
    """

    cur.execute(
        query,
        (
            data["product_name"],
            data["category"],
            data["price"],
            data["stock"],
            product_id
        )
    )

    con.commit()

    cur.close()
    con.close()

    return jsonify({
        "message": "Product updated successfully"
    })


@app.route("/products/delete/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):

    con = get_connection()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM products WHERE product_id = %s",
        (product_id,)
    )

    con.commit()

    cur.close()
    con.close()

    return jsonify({
        "message": "Product deleted successfully"
    })
@app.route("/customers")
def get_customers():

    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        SELECT customer_id, customer_name, phone, email
        FROM customers
    """)

    customers = cur.fetchall()

    customer_list = []

    for customer in customers:

        customer_list.append({
            "customer_id": customer[0],
            "customer_name": customer[1],
            "phone": customer[2],
            "email": customer[3]
        })

    cur.close()
    con.close()

    return jsonify(customer_list)


@app.route("/customers/add", methods=["POST"])
def add_customer_api():

    data = request.get_json()

    con = get_connection()
    cur = con.cursor()

    query = """
    INSERT INTO customers
    (customer_name, phone, email)
    VALUES (%s, %s, %s)
    """

    cur.execute(
        query,
        (
            data["customer_name"],
            data["phone"],
            data["email"]
        )
    )

    con.commit()

    cur.close()
    con.close()

    return jsonify({
        "message": "Customer added successfully"
    })


@app.route("/customers/update/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):

    data = request.get_json()

    con = get_connection()
    cur = con.cursor()

    query = """
    UPDATE customers
    SET customer_name = %s,
        phone = %s,
        email = %s
    WHERE customer_id = %s
    """

    cur.execute(
        query,
        (
            data["customer_name"],
            data["phone"],
            data["email"],
            customer_id
        )
    )

    con.commit()

    cur.close()
    con.close()

    return jsonify({
        "message": "Customer updated successfully"
    })


@app.route("/customers/delete/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):

    con = get_connection()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM customers WHERE customer_id = %s",
        (customer_id,)
    )

    con.commit()

    cur.close()
    con.close()

    return jsonify({
        "message": "Customer deleted successfully"
    })
@app.route("/suppliers")
def get_suppliers():

    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        SELECT supplier_id, supplier_name, phone, email
        FROM suppliers
    """)

    suppliers = cur.fetchall()

    supplier_list = []

    for supplier in suppliers:

        supplier_data = {
            "supplier_id": supplier[0],
            "supplier_name": supplier[1],
            "phone": supplier[2],
            "email": supplier[3]
        }

        supplier_list.append(supplier_data)

    cur.close()
    con.close()

    return jsonify(supplier_list)


@app.route("/suppliers/add", methods=["POST"])
def add_supplier_api():

    data = request.get_json()

    supplier_name = data["supplier_name"]
    phone = data["phone"]
    email = data["email"]

    con = get_connection()
    cur = con.cursor()

    query = """
    INSERT INTO suppliers
    (supplier_name, phone, email)
    VALUES (%s, %s, %s)
    """

    cur.execute(
        query,
        (supplier_name, phone, email)
    )

    con.commit()

    cur.close()
    con.close()

    return jsonify({
        "message": "Supplier added successfully"
    })


@app.route("/suppliers/update/<int:supplier_id>", methods=["PUT"])
def update_supplier(supplier_id):

    data = request.get_json()

    con = get_connection()
    cur = con.cursor()

    query = """
    UPDATE suppliers
    SET supplier_name = %s,
        phone = %s,
        email = %s
    WHERE supplier_id = %s
    """

    values = (
        data["supplier_name"],
        data["phone"],
        data["email"],
        supplier_id
    )

    cur.execute(query, values)

    con.commit()

    cur.close()
    con.close()

    return jsonify({
        "message": "Supplier updated successfully"
    })


@app.route("/suppliers/delete/<int:supplier_id>", methods=["DELETE"])
def delete_supplier(supplier_id):

    con = get_connection()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM suppliers WHERE supplier_id = %s",
        (supplier_id,)
    )

    con.commit()

    cur.close()
    con.close()

    return jsonify({
        "message": "Supplier deleted successfully"
    })
# ===============================
# PURCHASE MANAGEMENT
# ===============================

@app.route("/purchases")
def get_purchases():

    con = get_connection()
    cur = con.cursor()

    query = """
    SELECT
        p.purchase_id,
        s.supplier_name,
        p.purchase_date,
        p.total_amount
    FROM purchases p
    JOIN suppliers s
    ON p.supplier_id = s.supplier_id
    ORDER BY p.purchase_id DESC
    """

    cur.execute(query)

    purchases = cur.fetchall()

    purchase_list = []

    for purchase in purchases:

        purchase_list.append({
            "purchase_id": purchase[0],
            "supplier_name": purchase[1],
            "purchase_date": str(purchase[2]),
            "total_amount": float(purchase[3])
        })

    cur.close()
    con.close()

    return jsonify(purchase_list)


@app.route("/purchases/add", methods=["POST"])
def add_purchase_api():

    data = request.get_json()

    supplier_id = data["supplier_id"]
    purchase_date = data["purchase_date"]

    con = get_connection()
    cur = con.cursor()

    # Check supplier
    cur.execute(
        "SELECT supplier_id FROM suppliers WHERE supplier_id = %s",
        (supplier_id,)
    )

    supplier = cur.fetchone()

    if supplier is None:

        cur.close()
        con.close()

        return jsonify({
            "message": "Supplier not found"
        }), 404

    # Create purchase
    query = """
    INSERT INTO purchases
    (supplier_id, purchase_date, total_amount)
    VALUES (%s, %s, %s)
    """

    cur.execute(
        query,
        (supplier_id, purchase_date, 0)
    )

    con.commit()

    purchase_id = cur.lastrowid

    cur.close()
    con.close()

    return jsonify({
        "message": "Purchase created successfully",
        "purchase_id": purchase_id
    })


@app.route("/purchase-items/add", methods=["POST"])
def add_purchase_item_api():

    data = request.get_json()

    purchase_id = data["purchase_id"]
    product_id = data["product_id"]
    quantity = data["quantity"]
    price = data["price"]

    con = get_connection()
    cur = con.cursor()

    # Check purchase
    cur.execute(
        "SELECT purchase_id FROM purchases WHERE purchase_id = %s",
        (purchase_id,)
    )

    purchase = cur.fetchone()

    if purchase is None:

        cur.close()
        con.close()

        return jsonify({
            "message": "Purchase not found"
        }), 404

    # Check product
    cur.execute(
        "SELECT product_id FROM products WHERE product_id = %s",
        (product_id,)
    )

    product = cur.fetchone()

    if product is None:

        cur.close()
        con.close()

        return jsonify({
            "message": "Product not found"
        }), 404

    if quantity <= 0:

        cur.close()
        con.close()

        return jsonify({
            "message": "Quantity must be greater than 0"
        }), 400

    if price <= 0:

        cur.close()
        con.close()

        return jsonify({
            "message": "Price must be greater than 0"
        }), 400

    # Calculate item total
    item_total = quantity * price

    # Insert purchase item
    query = """
    INSERT INTO purchase_items
    (purchase_id, product_id, quantity, price)
    VALUES (%s, %s, %s, %s)
    """

    cur.execute(
        query,
        (
            purchase_id,
            product_id,
            quantity,
            price
        )
    )

    # Increase stock
    cur.execute(
        """
        UPDATE products
        SET stock = stock + %s
        WHERE product_id = %s
        """,
        (quantity, product_id)
    )

    # Update purchase total
    cur.execute(
        """
        UPDATE purchases
        SET total_amount = total_amount + %s
        WHERE purchase_id = %s
        """,
        (item_total, purchase_id)
    )

    con.commit()

    cur.close()
    con.close()

    return jsonify({
        "message": "Purchase item added successfully",
        "item_total": item_total
    })


@app.route("/purchase-items")
def get_purchase_items():

    con = get_connection()
    cur = con.cursor()

    query = """
    SELECT
        pi.purchase_item_id,
        pi.purchase_id,
        p.product_name,
        pi.quantity,
        pi.price
    FROM purchase_items pi
    JOIN products p
    ON pi.product_id = p.product_id
    ORDER BY pi.purchase_item_id DESC
    """

    cur.execute(query)

    items = cur.fetchall()

    item_list = []

    for item in items:

        item_list.append({
            "purchase_item_id": item[0],
            "purchase_id": item[1],
            "product_name": item[2],
            "quantity": item[3],
            "price": float(item[4])
        })

    cur.close()
    con.close()

    return jsonify(item_list)
if __name__ == "__main__":
    app.run(debug=True)
