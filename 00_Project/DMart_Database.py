import sqlite3

con = sqlite3.connect('DMart_Database.db')
cur = con.cursor()
cur.execute("PRAGMA foreign_keys = ON")         # ON DELETE CASCADE 

# print("\n===============DMART DATABASE CONECTED===============\n")

# ---------------------------------
# USER
# ---------------------------------
cur.execute("""
        CREATE TABLE IF NOT EXISTS USER(
            U_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            U_NAME TEXT NOT NULL,
            U_EMAIL TEXT NOT NULL,
            U_PASSWORD TEXT NOT NULL
    )
""")
con.commit()

# ---------------------------------
# PRODUCTS
# ---------------------------------
cur.execute("""
        CREATE TABLE IF NOT EXISTS PRODUCTS(
            PRO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PRO_NAME TEXT NOT NULL UNIQUE,
            PRO_PRICE REAL NOT NULL CHECK(PRO_PRICE > 0),
            PRO_AVAILABLE_QUANTITY INTEGER DEFAULT 0 CHECK(PRO_AVAILABLE_QUANTITY >= 0),
            PRO_DISCOUNT REAL NOT NULL DEFAULT 0 CHECK(PRO_DISCOUNT >= 0)
        )
""")
con.commit()

# ---------------------------------
# CART
# ---------------------------------
cur.execute("""
        CREATE TABLE IF NOT EXISTS CART(
            CART_ITEM_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USER_ID INTEGER NOT NULL,
            PRODUCT_ID INTEGER NOT NULL,
            QUANTITY INTEGER CHECK(QUANTITY > 0),  
            FOREIGN KEY(USER_ID) REFERENCES USER(U_ID) ON DELETE CASCADE,
            FOREIGN KEY(PRODUCT_ID) REFERENCES PRODUCTS(PRO_ID) ON DELETE CASCADE
    )
""")
con.commit()


# ---------------------------------
# ORDERS
# ---------------------------------

cur.execute("""
        CREATE TABLE IF NOT EXISTS ORDERS (
            ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USER_ID INTEGER NOT NULL,
            DELIVERY_PHONE TEXT NOT NULL CHECK(length(DELIVERY_PHONE) = 10),
            DELIVERY_ADDRESS TEXT NOT NULL,
            TOTAL_AMOUNT REAL NOT NULL,
            ORDER_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(USER_ID) REFERENCES USER(U_ID) ON DELETE CASCADE
    )
""")
con.commit()