# OptiManage Inventory Management System

OptiManage is a simple command-line Inventory Management System built using Python and SQLite. It allows users to manage products, track inventory levels, and receive low-stock alerts through an easy-to-use terminal interface.

## Features

- View current inventory
- Add new products
- Store inventory data using SQLite
- Unique SKU validation
- Low stock alerts
- Simple command-line dashboard
- Lightweight and beginner-friendly

## Technologies Used

- Python 3
- SQLite3

## Project Structure

```text
git/
│
├── main.py
├── database.py
├── inventory.db
└── README.md
```

## Database Schema

The application uses a SQLite database named `inventory.db`.

### Products Table

| Column | Type | Description |
|----------|----------|-------------|
| id | INTEGER | Primary Key |
| name | TEXT | Product Name |
| sku | TEXT | Unique Product Code |
| quantity | INTEGER | Available Stock |
| price | REAL | Price Per Unit |
| min_stock_level | INTEGER | Minimum Stock Threshold |

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/a73640947-droid/git.git
cd git
```

### 2. Verify Python Installation

```bash
python --version
```

### 3. Run the Application

```bash
python main.py
```

## Usage

When the application starts, you will see the dashboard menu:

```text
=========================
  OPTIMANAGE DASHBOARD
=========================
1. View Current Inventory
2. Add New Product
3. Exit
```

### View Inventory

Displays all products stored in the database along with:

- Product ID
- Product Name
- SKU
- Quantity
- Price
- Stock Status

Products with quantity less than or equal to the minimum stock level are marked as:

```text
⚠️ LOW STOCK
```

### Add Product

Users can add a new product by entering:

- Product Name
- SKU
- Quantity
- Price
- Minimum Stock Level

The system automatically prevents duplicate SKUs.

## Example Output

```text
--- CURRENT INVENTORY ---

ID    Name                 SKU        Qty      Price      Status
-----------------------------------------------------------------
1     Pen                  PEN001     50       10.0       OK
2     Notebook             NB001      5        40.0       ⚠️ LOW STOCK
```

## Error Handling

The application includes:

- Duplicate SKU detection
- Database exception handling
- Input validation for menu choices

## Future Improvements

Planned features include:

- Update product information
- Delete products
- Search products
- Sales tracking
- Purchase management
- Inventory reports
- CSV export/import
- Graphical User Interface (GUI)
- Web-based dashboard

## Learning Objectives

This project demonstrates:

- Python programming fundamentals
- Function-based program design
- SQLite database integration
- CRUD operations
- Exception handling
- Command-line application development

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push to your fork
6. Open a Pull Request

## License

This project is open-source and available for educational purposes.

## Repository

GitHub Repository:

https://github.com/a73640947-droid/git

## Author

Ansul

---

Built with Python and SQLite for simple inventory management.
