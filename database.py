
import sqlite3

def init_db():
    # Database file se connect karein (agar nahi hai toh khud ban jayegi)
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    
    # 1. Products Table banayein
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sku TEXT UNIQUE NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            min_stock_level INTEGER DEFAULT 5
        )
    ''')
    
    # 2. Orders Table banayein
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER,
            order_date TEXT,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY(product_id) REFERENCES products(product_id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database aur Tables safaltapoorvak ban gaye hain!")

if __name__ == "__main__":
    init_db()