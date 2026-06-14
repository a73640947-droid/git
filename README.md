# OptiManage Inventory Management System

OptiManage is a lightweight Inventory Management System built using Python and SQLite. The application provides a simple command-line interface for managing products, monitoring stock levels, and maintaining inventory records.

## Features

* View current inventory
* Add new products
* Store data using SQLite database
* Unique SKU validation
* Low-stock alerts
* Simple and user-friendly command-line interface

## Technologies Used

* Python 3
* SQLite3

## Project Structure

```text
.
├── main.py
├── database.py
├── README.md
└── .gitignore
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/a73640947-droid/git.git
cd git
```

### Run the Application

```bash
python main.py
```

## Usage

After running the application, the following menu will be displayed:

```text
=========================
  OPTIMANAGE DASHBOARD
=========================
1. View Current Inventory
2. Add New Product
3. Exit
```

### View Inventory

Displays all products stored in the database, including:

* Product ID
* Product Name
* SKU
* Quantity
* Price
* Stock Status

Products with quantity less than or equal to the minimum stock level are automatically marked as **LOW STOCK**.

### Add Product

Users can add new products by entering:

* Product Name
* SKU
* Quantity
* Price per Unit
* Minimum Stock Level

Duplicate SKUs are prevented to maintain data integrity.

## Example Output

```text
--- CURRENT INVENTORY ---

ID    Name                 SKU        Qty      Price      Status
-----------------------------------------------------------------
1     Pen                  PEN001     50       10.0       OK
2     Notebook             NB001      5        40.0       LOW STOCK
```

## Future Enhancements

* Update product details
* Delete products
* Product search functionality
* Sales tracking
* Inventory reports
* CSV import/export
* Graphical User Interface (GUI)
* Web dashboard

## Learning Outcomes

This project demonstrates:

* Python programming fundamentals
* SQLite database operations
* CRUD functionality
* Exception handling
* Command-line application development

## Author

Ansul

## License

This project is available for educational and learning purposes.









