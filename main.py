from products import add_product, view_products
from customers import add_customer, view_customers
from suppliers import add_supplier, view_suppliers
from purchases import add_purchase, view_purchase, add_purchase_item, view_purchase_items
from sales import add_sale, add_sale_item, view_sales, view_sale_items
from reports import (
    total_sales_report,
    number_of_sales_report,
    best_selling_products_report,
    low_stock_report,
    customer_purchase_history,
    monthly_sales_report
)

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Add Customer")
    print("4. View Customers")
    print("5. Add Supplier")
    print("6. View Suppliers")
    print("7. Add Purchase")
    print("8. View Purchase")
    print("9. Add Purchase Item")
    print("10. View Purchase Items")
    print("11. Add Sale")
    print("12. Add Sale Item")
    print("13. View Sales")
    print("14. View Sale Items")
    print("15. Total Sales Report")
    print("16. Number of Sales Report")
    print("17. Best-Selling Products Report")
    print("18. Low Stock Report")
    print("19. Customer Purchase History")
    print("20. Monthly Sales Report")
    print("21. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if choice == 1:
        add_product()

    elif choice == 2:
        view_products()

    elif choice == 3:
        add_customer()

    elif choice == 4:
        view_customers()

    elif choice == 5:
        add_supplier()

    elif choice == 6:
        view_suppliers()

    elif choice == 7:
        add_purchase()

    elif choice == 8:
        view_purchase()

    elif choice == 9:
        add_purchase_item()

    elif choice == 10:
        view_purchase_items()

    elif choice == 11:
        add_sale()

    elif choice == 12:
        add_sale_item()

    elif choice == 13:
        view_sales()

    elif choice == 14:
        view_sale_items()

    elif choice == 15:
        total_sales_report()

    elif choice == 16:
        number_of_sales_report()

    elif choice == 17:
        best_selling_products_report()

    elif choice == 18:
        low_stock_report()

    elif choice == 19:
        customer_purchase_history()

    elif choice == 20:
        monthly_sales_report()

    elif choice == 21:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
