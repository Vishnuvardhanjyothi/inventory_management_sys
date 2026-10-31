// Get all sidebar menu buttons
const menuItems = document.querySelectorAll(".menu-item[data-page]");

// Get all pages
const pages = document.querySelectorAll(".page");

// Get page title elements
const pageTitle = document.querySelector(".page-title h1");
const pageDescription = document.querySelector(".page-title p");


// Page information
const pageInfo = {
    dashboard: {
        title: "Dashboard",
        description: "Overview of your inventory and sales"
    },

    products: {
        title: "Products",
        description: "Manage your products and stock"
    },

    customers: {
        title: "Customers",
        description: "Manage customer information"
    },

    suppliers: {
        title: "Suppliers",
        description: "Manage supplier information"
    },

    purchases: {
        title: "Purchases",
        description: "Manage purchases and stock updates"
    },

    sales: {
        title: "Sales & Billing",
        description: "Create and manage sales"
    },

    reports: {
        title: "Reports",
        description: "View sales and inventory reports"
    }
};


// Add click event to each menu item
menuItems.forEach(function(menuItem) {

    menuItem.addEventListener("click", function() {

        // Get the page name
        const pageName = menuItem.getAttribute("data-page");


        // Remove active class from all menu items
        menuItems.forEach(function(item) {
            item.classList.remove("active");
        });


        // Add active class to clicked menu item
        menuItem.classList.add("active");


        // Hide all pages
        pages.forEach(function(page) {
            page.classList.remove("active-page");
        });


        // Show selected page
        const selectedPage = document.getElementById(pageName);

        if (selectedPage) {
            selectedPage.classList.add("active-page");
        }


        // Update page title
        if (pageInfo[pageName]) {

            pageTitle.textContent = pageInfo[pageName].title;

            pageDescription.textContent = pageInfo[pageName].description;
        }

    });

});
async function loadProducts() {
    try {
        const response = await fetch("http://127.0.0.1:5000/products");

        const products = await response.json();

        const productTable = document.querySelector("#products table tbody");

        productTable.innerHTML = "";

        products.forEach(function(product) {

            let status = "";

            if (product.stock === 0) {
                status = '<span class="status out-stock">Out of Stock</span>';
            }
            else if (product.stock < 10) {
                status = '<span class="status low-stock">Low Stock</span>';
            }
            else {
                status = '<span class="status available">Available</span>';
            }

            const row = `
                <tr>
                    <td>${product.product_id}</td>
                    <td>${product.product_name}</td>
                    <td>${product.category}</td>
                    <td>₹${product.price}</td>
                    <td>${product.stock}</td>
                    <td>${status}</td>
                    <td>
                        <button class="edit-button" onclick="editProduct(${product.product_id})">
    Edit
</button>
                        <button class="delete-button"
        onclick="deleteProduct(${product.product_id})">
    Delete
</button>
                    </td>
                </tr>
            `;

            productTable.innerHTML += row;
        });

    }
    catch (error) {
        console.log("Error loading products:", error);
    }
}

loadProducts();
const addProductBtn = document.getElementById("addProductBtn");
const productFormContainer = document.getElementById("productFormContainer");
const closeProductForm = document.getElementById("closeProductForm");


addProductBtn.addEventListener("click", function() {

    productFormContainer.classList.add("show");

});


closeProductForm.addEventListener("click", function() {

    productFormContainer.classList.remove("show");

});
const productForm = document.getElementById("productForm");

productForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const productName = document.getElementById("productName").value;
    const category = document.getElementById("productCategory").value;
    const price = document.getElementById("productPrice").value;
    const stock = document.getElementById("productStock").value;

    const productData = {
        product_name: productName,
        category: category,
        price: Number(price),
        stock: Number(stock)
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/products/add",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(productData)
            }
        );

        const result = await response.json();

        alert(result.message);

        productForm.reset();

        productFormContainer.classList.remove("show");

        loadProducts();

    }
    catch (error) {

        console.log("Error adding product:", error);

        alert("Unable to add product");

    }

});
async function editProduct(productId) {

    const productName = prompt("Enter product name:");
    const category = prompt("Enter category:");
    const price = prompt("Enter price:");
    const stock = prompt("Enter stock:");

    if (
        productName === null ||
        category === null ||
        price === null ||
        stock === null
    ) {
        return;
    }

    const productData = {
        product_name: productName,
        category: category,
        price: Number(price),
        stock: Number(stock)
    };

    try {

        const response = await fetch(
            `http://127.0.0.1:5000/products/update/${productId}`,
            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(productData)
            }
        );

        const result = await response.json();

        alert(result.message);

        loadProducts();

    }
    catch (error) {

        console.log("Error updating product:", error);

        alert("Unable to update product");

    }
}
async function deleteProduct(productId) {

    const confirmDelete = confirm(
        "Are you sure you want to delete this product?"
    );

    if (!confirmDelete) {
        return;
    }

    try {

        const response = await fetch(
            `http://127.0.0.1:5000/products/delete/${productId}`,
            {
                method: "DELETE"
            }
        );

        const result = await response.json();

        alert(result.message);

        loadProducts();

    }
    catch (error) {

        console.log("Error deleting product:", error);

        alert("Unable to delete product");

    }
}
async function loadCustomers() {

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/customers"
        );

        const customers = await response.json();

        const customerTable =
            document.querySelector("#customers table tbody");

        customerTable.innerHTML = "";


        customers.forEach(function(customer) {

            const row = `
                <tr>

                    <td>${customer.customer_id}</td>

                    <td>${customer.customer_name}</td>

                    <td>${customer.phone}</td>

                    <td>${customer.email}</td>

                    <td>

                        <button
                            class="edit-button"
                            onclick="editCustomer(${customer.customer_id})">
                            Edit
                        </button>

                        <button
                            class="delete-button"
                            onclick="deleteCustomer(${customer.customer_id})">
                            Delete
                        </button>

                    </td>

                </tr>
            `;

            customerTable.innerHTML += row;

        });

    }

    catch (error) {

        console.log(
            "Error loading customers:",
            error
        );

    }

}

loadCustomers();
// ===============================
// CUSTOMER MANAGEMENT
// ===============================

const addCustomerBtn =
    document.getElementById("addCustomerBtn");

const customerFormContainer =
    document.getElementById("customerFormContainer");

const closeCustomerForm =
    document.getElementById("closeCustomerForm");


// Open customer form
addCustomerBtn.addEventListener("click", function() {

    customerFormContainer.classList.add("show");

});


// Close customer form
closeCustomerForm.addEventListener("click", function() {

    customerFormContainer.classList.remove("show");

});


// Add customer
const customerForm =
    document.getElementById("customerForm");

customerForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const customerName =
        document.getElementById("customerName").value;

    const customerPhone =
        document.getElementById("customerPhone").value;

    const customerEmail =
        document.getElementById("customerEmail").value;


    const customerData = {

        customer_name: customerName,
        phone: customerPhone,
        email: customerEmail

    };


    try {

        const response = await fetch(
            "http://127.0.0.1:5000/customers/add",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(customerData)
            }
        );


        const result = await response.json();

        alert(result.message);

        customerForm.reset();

        customerFormContainer.classList.remove("show");

        loadCustomers();

    }

    catch (error) {

        console.log("Error adding customer:", error);

        alert("Unable to add customer");

    }

});


// Edit customer
async function editCustomer(customerId) {

    const customerName =
        prompt("Enter customer name:");

    const phone =
        prompt("Enter phone:");

    const email =
        prompt("Enter email:");


    if (
        customerName === null ||
        phone === null ||
        email === null
    ) {
        return;
    }


    const customerData = {

        customer_name: customerName,
        phone: phone,
        email: email

    };


    try {

        const response = await fetch(

            `http://127.0.0.1:5000/customers/update/${customerId}`,

            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(customerData)
            }

        );


        const result = await response.json();

        alert(result.message);

        loadCustomers();

    }

    catch (error) {

        console.log("Error updating customer:", error);

        alert("Unable to update customer");

    }

}


// Delete customer
async function deleteCustomer(customerId) {

    const confirmDelete = confirm(
        "Are you sure you want to delete this customer?"
    );


    if (!confirmDelete) {

        return;

    }


    try {

        const response = await fetch(

            `http://127.0.0.1:5000/customers/delete/${customerId}`,

            {
                method: "DELETE"
            }

        );


        const result = await response.json();

        alert(result.message);

        loadCustomers();

    }

    catch (error) {

        console.log("Error deleting customer:", error);

        alert("Unable to delete customer");

    }

}

// ===============================
// SUPPLIER MANAGEMENT
// ===============================

async function loadSuppliers() {

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/suppliers"
        );

        const suppliers = await response.json();

        const supplierTable =
            document.querySelector("#suppliers table tbody");

        supplierTable.innerHTML = "";

        suppliers.forEach(function(supplier) {

            const row = `
                <tr>
                    <td>${supplier.supplier_id}</td>
                    <td>${supplier.supplier_name}</td>
                    <td>${supplier.phone}</td>
                    <td>${supplier.email}</td>

                    <td>
                        <button
                            class="edit-button"
                            onclick="editSupplier(${supplier.supplier_id})">
                            Edit
                        </button>

                        <button
                            class="delete-button"
                            onclick="deleteSupplier(${supplier.supplier_id})">
                            Delete
                        </button>
                    </td>
                </tr>
            `;

            supplierTable.innerHTML += row;

        });

    }

    catch (error) {

        console.log("Error loading suppliers:", error);

    }

}

loadSuppliers();


// Open form
document
    .getElementById("addSupplierBtn")
    .addEventListener("click", function() {

        document
            .getElementById("supplierFormContainer")
            .classList.add("show");

    });


// Close form
document
    .getElementById("closeSupplierForm")
    .addEventListener("click", function() {

        document
            .getElementById("supplierFormContainer")
            .classList.remove("show");

    });


// Add supplier
document
    .getElementById("supplierForm")
    .addEventListener("submit", async function(event) {

        event.preventDefault();

        const supplierData = {

            supplier_name:
                document.getElementById("supplierName").value,

            phone:
                document.getElementById("supplierPhone").value,

            email:
                document.getElementById("supplierEmail").value

        };

        try {

            const response = await fetch(
                "http://127.0.0.1:5000/suppliers/add",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(supplierData)
                }
            );

            const result = await response.json();

            alert(result.message);

            document
                .getElementById("supplierForm")
                .reset();

            document
                .getElementById("supplierFormContainer")
                .classList.remove("show");

            loadSuppliers();

        }

        catch (error) {

            console.log("Error adding supplier:", error);

            alert("Unable to add supplier");

        }

    });


// Edit supplier
async function editSupplier(supplierId) {

    const supplierName = prompt("Enter supplier name:");
    const phone = prompt("Enter phone:");
    const email = prompt("Enter email:");

    if (
        supplierName === null ||
        phone === null ||
        email === null
    ) {
        return;
    }

    const supplierData = {

        supplier_name: supplierName,
        phone: phone,
        email: email

    };

    try {

        const response = await fetch(

            `http://127.0.0.1:5000/suppliers/update/${supplierId}`,

            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(supplierData)
            }

        );

        const result = await response.json();

        alert(result.message);

        loadSuppliers();

    }

    catch (error) {

        console.log("Error updating supplier:", error);

        alert("Unable to update supplier");

    }

}


// Delete supplier
async function deleteSupplier(supplierId) {

    const confirmDelete = confirm(
        "Are you sure you want to delete this supplier?"
    );

    if (!confirmDelete) {
        return;
    }

    try {

        const response = await fetch(

            `http://127.0.0.1:5000/suppliers/delete/${supplierId}`,

            {
                method: "DELETE"
            }

        );

        const result = await response.json();

        alert(result.message);

        loadSuppliers();

    }

    catch (error) {

        console.log("Error deleting supplier:", error);

        alert("Unable to delete supplier");

    }

}
// ===============================
// PURCHASE MANAGEMENT
// ===============================

async function loadPurchases() {

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/purchases"
        );

        const purchases = await response.json();

        const tableBody =
            document.getElementById("purchaseTableBody");

        tableBody.innerHTML = "";

        purchases.forEach(function(purchase) {

            const row = `
                <tr>

                    <td>${purchase.purchase_id}</td>

                    <td>${purchase.supplier_name}</td>

                    <td>${purchase.purchase_date}</td>

                    <td>₹${purchase.total_amount}</td>

                </tr>
            `;

            tableBody.innerHTML += row;

        });

    }

    catch (error) {

        console.log(
            "Error loading purchases:",
            error
        );

    }

}

loadPurchases();


// Open purchase form
document
    .getElementById("addPurchaseBtn")
    .addEventListener("click", function() {

        document
            .getElementById("purchaseFormContainer")
            .classList.add("show");

    });


// Close purchase form
document
    .getElementById("closePurchaseForm")
    .addEventListener("click", function() {

        document
            .getElementById("purchaseFormContainer")
            .classList.remove("show");

    });


// Create purchase
document
    .getElementById("purchaseForm")
    .addEventListener("submit", async function(event) {

        event.preventDefault();

        const supplierId =
            Number(
                document.getElementById(
                    "purchaseSupplierId"
                ).value
            );

        const purchaseDate =
            document.getElementById(
                "purchaseDate"
            ).value;


        const purchaseData = {

            supplier_id: supplierId,
            purchase_date: purchaseDate

        };


        try {

            const response = await fetch(

                "http://127.0.0.1:5000/purchases/add",

                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(
                        purchaseData
                    )
                }

            );


            const result =
                await response.json();


            alert(
                result.message +
                (
                    result.purchase_id
                    ? "\nPurchase ID: " +
                      result.purchase_id
                    : ""
                )
            );


            document
                .getElementById("purchaseForm")
                .reset();


            document
                .getElementById(
                    "purchaseFormContainer"
                )
                .classList.remove("show");


            loadPurchases();

        }

        catch (error) {

            console.log(
                "Error creating purchase:",
                error
            );

            alert(
                "Unable to create purchase"
            );

        }

    });
    // ===============================
// PURCHASE ITEM MANAGEMENT
// ===============================

async function loadPurchaseItems() {

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/purchase-items"
        );

        const items = await response.json();

        console.log("Purchase Items:", items);

    }

    catch (error) {

        console.log(
            "Error loading purchase items:",
            error
        );

    }

}

loadPurchaseItems();


// Open form
document
    .getElementById("addPurchaseItemBtn")
    .addEventListener("click", function() {

        document
            .getElementById(
                "purchaseItemFormContainer"
            )
            .classList.add("show");

    });


// Close form
document
    .getElementById("closePurchaseItemForm")
    .addEventListener("click", function() {

        document
            .getElementById(
                "purchaseItemFormContainer"
            )
            .classList.remove("show");

    });


// Add purchase item
document
    .getElementById("purchaseItemForm")
    .addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            const purchaseId =
                Number(
                    document.getElementById(
                        "purchaseItemPurchaseId"
                    ).value
                );


            const productId =
                Number(
                    document.getElementById(
                        "purchaseItemProductId"
                    ).value
                );


            const quantity =
                Number(
                    document.getElementById(
                        "purchaseItemQuantity"
                    ).value
                );


            const price =
                Number(
                    document.getElementById(
                        "purchaseItemPrice"
                    ).value
                );


            const purchaseItemData = {

                purchase_id: purchaseId,
                product_id: productId,
                quantity: quantity,
                price: price

            };


            try {

                const response = await fetch(

                    "http://127.0.0.1:5000/purchase-items/add",

                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify(
                            purchaseItemData
                        )
                    }

                );


                const result =
                    await response.json();


                alert(
                    result.message +
                    (
                        result.item_total
                        ? "\nItem Total: ₹" +
                          result.item_total
                        : ""
                    )
                );


                document
                    .getElementById(
                        "purchaseItemForm"
                    )
                    .reset();


                document
                    .getElementById(
                        "purchaseItemFormContainer"
                    )
                    .classList.remove("show");


                loadPurchases();


            }

            catch (error) {

                console.log(
                    "Error adding purchase item:",
                    error
                );

                alert(
                    "Unable to add purchase item"
                );

            }

        }
    );
loadPurchases();
loadProducts();