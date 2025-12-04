import sqlite3

con = sqlite3.connect('Transaction.db')
cur = con.cursor()

cur.execute("PRAGMA foreign_keys = ON")

print("Connected to Transaction database sucessfully...")

print("\n-------------------------------\n")

cur.execute("""
        CREATE TABLE IF NOT EXISTS CUSTOMER(
            C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            C_NAME TEXT NOT NULL,
            C_ADDRESS TEXT NOT NULL,
            C_CONTACT INTEGER NOT NULL
        )
""")
con.commit()


cur.execute("""
        CREATE TABLE IF NOT EXISTS ACCOUNT (
            A_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CUSTOMER_ID INTEGER NOT NULL,
            BALANCE REAL DEFAULT 0,
            FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(C_ID) ON DELETE CASCADE
        )
""")
# ON DELETE CASCADE → If customer is deleted → account also deletedcon.commit()

print("CUSTOMER and ACCOUNT table created sucessfully...")

print("\n-------------------------------\n")

# cur.execute("""
#         INSERT INTO CUSTOMER (C_NAME, C_ADDRESS, C_CONTACT) VALUES
#             ('Aditi', 'Surat', 9876543210),
#             ('Rahul', 'Ahmedabad', 9123456780),
#             ('Meera', 'Vadodara', 9988776655),
#             ('John', 'Surat', 9871122334),
#             ('Sara', 'Rajkot', 9001122334),
#             ('Priya', 'Ahmedabad', 9122334455) 
# """)
# con.commit()
print("CUSTOMER table data inserted successfully...")

print("\n-------------------------------\n")

# cur.execute("""
#     INSERT INTO ACCOUNT (CUSTOMER_ID, BALANCE) VALUES
#     (1, 5000.0),
#     (2, 10000.0),
#     (3, 7500.5),
#     (4, 2000.0),
#     (5, 0.0),
#     (6, 12000.0)
# """)
# con.commit()
print("ACCOUNT table data inserted successfully...")

print("\n-------------------------------\n")



# # -------------------------
# # Transfer ₹1000 from Aditi → Rahul
# # -------------------------

# try:
#     cur.execute("BEGIN")        # Start transaction
    
#     cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE - 1000 WHERE A_ID = 1")
#     cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE + 1000 WHERE A_ID = 2")

#     con.commit()    # Save 

#     print("Transfer successful!")

# except Exception as e:
#     con.rollback()   # UNDO
#     print(e)



# print("\n-------------------------------\n")


# # -------------------------
# # Deposit ₹2000 into Aditi account
# # -------------------------

# try:
#     cur.execute("BEGIN")        # Start transaction
    
#     cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE + 2000 WHERE A_ID = 1")
#     con.commit()    # Save 

#     print("Deposit successful!")

# except Exception as e:
#     con.rollback()   # UNDO
#     print(e)

# print("\n-------------------------------\n")

# -------------------------
# Withdraw ₹1500 from Priya’s account
# -------------------------
try:
    cur.execute("UPDATE ACCOUNT SET BALANCE = BALANCE - 1500 WHERE A_ID = 6")

    con.commit()
    print("Withdraw 1500 rs sucessfully from priyas account...")
except Exception as e:
    con.rollback()   # UNDO
    print(e)

con.close()