from database import con, cur


def total_sales_report():
    query = """
    SELECT SUM(total_amount)
    FROM sales
    """

    cur.execute(query)
    data = cur.fetchone()

    print("Total Sales:", data[0])



def number_of_sales_report():
    query = """
    SELECT COUNT(*)
    FROM sales
    """

    cur.execute(query)

    data = cur.fetchone()

    print("Total Number of Sales:", data[0])


def best_selling_products_report():
    query = """
    SELECT
        p.product_name,
        SUM(si.quantity) AS total_quantity
    FROM sale_items si
    JOIN products p
    ON si.product_id = p.product_id
    GROUP BY p.product_id, p.product_name
    ORDER BY total_quantity DESC
    """

    cur.execute(query)

    data = cur.fetchall()

    print("\nBest-Selling Products")
    print("----------------------")

    for product in data:
        print("Product:", product[0])
        print("Quantity Sold:", product[1])
        print("----------------------")


def low_stock_report():
    query = """
    SELECT *
    FROM products
    WHERE stock < 10
    """

    cur.execute(query)

    data = cur.fetchall()

    print("\nLow Stock Products")
    print("------------------")

    for product in data:
        print("ID:", product[0])
        print("Name:", product[1])
        print("Category:", product[2])
        print("Price:", product[3])
        print("Stock:", product[4])
        print("------------------")


def customer_purchase_history():
    customer_id = int(input("Enter customer ID: "))

    query = """
    SELECT
        c.customer_name,
        p.product_name,
        si.quantity,
        si.price,
        s.sale_date
    FROM customers c
    JOIN sales s
    ON c.customer_id = s.customer_id
    JOIN sale_items si
    ON s.sale_id = si.sale_id
    JOIN products p
    ON si.product_id = p.product_id
    WHERE c.customer_id = %s
    """

    cur.execute(query, (customer_id,))

    data = cur.fetchall()

    if len(data) == 0:
        print("No purchase history found")
        return

    print("\nCustomer Purchase History")
    print("-------------------------")

    for purchase in data:
        print("Customer:", purchase[0])
        print("Product:", purchase[1])
        print("Quantity:", purchase[2])
        print("Price:", purchase[3])
        print("Date:", purchase[4])
        print("-------------------------")


def monthly_sales_report():
    query = """
    SELECT
        MONTH(sale_date) AS month,
        SUM(total_amount) AS total_sales
    FROM sales
    GROUP BY MONTH(sale_date)
    ORDER BY month
    """

    cur.execute(query)

    data = cur.fetchall()

    print("\nMonthly Sales Report")
    print("--------------------")

    for report in data:
        print("Month:", report[0])
        print("Total Sales:", report[1])
        print("--------------------")
