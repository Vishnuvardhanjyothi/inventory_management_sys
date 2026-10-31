# Inventory & Sales Management System

A web-based Inventory & Sales Management System developed using Python, Flask, MySQL, HTML, CSS, and JavaScript. This application helps manage products, customers, suppliers, purchases, sales, and inventory stock efficiently.

## 🚀 Features

- **Dashboard:** Centralized navigation to all modules.
- **Product Management:** Add, view, update, and delete products.
- **Customer Management:** Maintain customer details.
- **Supplier Management:** Manage supplier information.
- **Purchase Management:** Record purchases and purchase items.
- **Automatic Stock Updates:** Increase product stock when purchases are recorded.
- **Sales Management:** Record sales and sale items.
- **Stock Management:** Track available product quantities.
- **Reports:** Generate sales and inventory reports.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Backend API development |
| MySQL | Database management |
| HTML | Frontend structure |
| CSS | Styling and layout |
| JavaScript | Frontend functionality |
| Flask-CORS | Frontend-backend communication |
| MySQL Connector | Python-MySQL connectivity |

## 📂 Project Structure

```text
inventory_management/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── app.py
├── database.py
├── products.py
├── customers.py
├── suppliers.py
├── purchases.py
├── sales.py
├── reports.py
├── main.py
│
└── README.md
```

## 🗄️ Database Design

The project uses MySQL with the following tables:

- users
- products
- customers
- suppliers
- purchases
- purchase_items
- sales
- sale_items

### Business Workflow

```text
Supplier
   ↓
Purchase
   ↓
Purchase Items
   ↓
Inventory Stock
   ↓
Sales
   ↓
Customer
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd inventory_management
```

### 3. Install Required Packages

```bash
python -m pip install flask flask-cors mysql-connector-python
```

### 4. Create the MySQL Database

```sql
CREATE DATABASE inventory_management;
```

Create the required tables using the SQL queries provided in the project.

### 5. Configure Database Connection

Update the MySQL connection details in your Python database configuration:

```python
host="localhost"
user="root"
password="YOUR_MYSQL_PASSWORD"
database="inventory_management"
```

Replace `YOUR_MYSQL_PASSWORD` with your MySQL password.

### 6. Run the Flask Application

```bash
python app.py
```

### 7. Open the Frontend

Open `frontend/index.html` in your browser.

Make sure the Flask backend is running before using the application.

## 📊 Key Learning Outcomes

- Python and MySQL database integration.
- CRUD operations using Python and Flask.
- REST API development.
- SQL queries, joins, and relational database concepts.
- Frontend and backend integration using JavaScript Fetch API.
- Inventory stock management and transaction processing.

## 🔮 Future Enhancements

- User authentication and role-based access.
- Dashboard with sales analytics and charts.
- Search and filter functionality.
- Export reports to PDF and Excel.
- Improved form validation and error handling.

## 👨‍💻 Author

**Vishnu Vardhan**

B.Tech – Electronics and Communication Engineering (2026)

**Project:** Inventory & Sales Management System
