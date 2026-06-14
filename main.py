import sqlite3

def view_inventory():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    
    print("\n--- CURRENT INVENTORY ---")
    print(f"{'ID':<5} {'Name':<20} {'SKU':<10} {'Qty':<8} {'Price':<10} {'Status'}")
    print("-" * 65)
    
    for row in rows:
        status = "OK"
        if row[3] <= row[5]: # Agar quantity min_stock_level se kam ya barabar hai
            status = "⚠️ LOW STOCK"
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<10} {row[3]:<8} {row[4]:<10} {status}")
    conn.close()

def add_product():
    print("\n--- ADD NEW PRODUCT ---")
    name = input("Product Name: ")
    sku = input("SKU (Unique Code): ")
    qty = int(input("Quantity: "))
    price = float(input("Price per unit: "))
    min_stock = int(input("Min Stock Level (Alert ke liye): "))
    
    try:
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, sku, quantity, price, min_stock_level) VALUES (?, ?, ?, ?, ?)", 
                       (name, sku, qty, price, min_stock))
        conn.commit()
        print(f"🎉 {name} ko inventory mein add kar diya gaya hai!")
    except sqlite3.IntegrityError:
        print("❌ Error: Yeh SKU pehle se exist karta hai!")
    finally:
        conn.close()

def main_menu():
    while True:
        print("\n=========================")
        print("  OPTIMANAGE DASHBOARD   ")
        print("=========================")
        print("1. View Current Inventory")
        print("2. Add New Product")
        print("3. Exit")
        
        choice = input("Apna option chunein (1-3): ")
        
        if choice == '1':
            view_inventory()
        elif choice == '2':
            add_product()
        elif choice == '3':
            print("OptiManage use karne ke liye dhanyawad. Bye!")
            break
        else:
            print("Galat option! Kripya 1, 2, ya 3 chunein.")

if __name__ == "__main__":
    main_menu()