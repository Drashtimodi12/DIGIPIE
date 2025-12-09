from DMart_Database import *
import re

# ---------------------------------
# sign_up()
# ---------------------------------
def sign_up():
    print("\n===== CREATE NEW ACCOUNT =====\n")

    user_name = input("Name:    ").strip()

    # Email Check
    user_email = input("Email:    ").strip()
    email_pattern = r"^[A-Za-z0-9._]+@[A-Za-z]+\.[A-Za-z]{2,}$"

    if not re.match(email_pattern, user_email):
        print("Invalid Email format! Example: user12@gmail.com")
        return
    
    cur.execute("SELECT * FROM USER WHERE U_EMAIL = ?", (user_email,))

    if cur.fetchone():
        print("Email already registered! Please LOG IN.")
        return 

    # Password Check
    user_password = input("Password:    ")
    password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

    if not re.match(password_pattern, user_password):
        print("""Password must contain:
              Ensures at least 1 uppercase letter, 1 lowercase letter, 1 digit, Minimum 8 characters.""")
        return

    # Insert user
    cur.execute("INSERT INTO USER(U_NAME, U_EMAIL, U_PASSWORD) VALUES (?, ?, ?)", (user_name, user_email, user_password))
    con.commit()

    print("Account create successfully!")


# ---------------------------------
# login()
# ---------------------------------
def login():
    print("\n===== LOG IN ACCOUNT =====\n")

    # Email Check
    login_email = input("Email:    ").strip()
    email_pattern = r"^[A-Za-z0-9._]+@[A-Za-z]+\.[A-Za-z]{2,}$"
    
    if not re.match(email_pattern, login_email):
        print("Invalid Email format! Example: user12@gmail.com")
        return
    
    cur.execute("SELECT * FROM USER WHERE U_EMAIL = ?", (login_email,))
    if cur.fetchone() is None:
        print("Email Not found! Please SIGN UP First.")
        return 

    # Password Check
    login_password = input("Password:    ").strip()
    password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

    if not re.match(password_pattern, login_password):
        print("""Password must contain:
              Ensures at least 1 uppercase letter, 1 lowercase letter, 1 digit, Minimum 8 characters.""")
        return

    cur.execute("SELECT * FROM USER WHERE U_EMAIL = ? AND U_PASSWORD = ?", (login_email, login_password))
    login_user = cur.fetchone()

    if login_user:
        print("\nLogin successfully! Welcome,", (login_user[1]))
        return login_user[0]
    else:
        print("\nIncorrect password! Try again.")
        return 
        
        
# ---------------------------------
# view_products()
# ---------------------------------
def view_products():
    print("\n========== AVAILABLE PRODUCTS ==========\n")

    cur.execute("SELECT * FROM PRODUCTS")
    products = cur.fetchall()

    if not products:
        print("No products found in store.")
        return
    
    for pro_id, name, price, quantity, discount in products:
            Discount_Amount = price * (discount / 100)
            Final_Price = price - Discount_Amount

            print(f""" - {pro_id} | {name} | Price: ₹{price} | Discount: {discount}% | Final Price: ₹{Final_Price} | Stock: {quantity} \n""")


# ---------------------------------
# add_to_cart()
# ---------------------------------
def add_to_cart():

    global current_user_id

    view_products()

    try:
        product_id = int(input("Enter Products id to add to cart: "))

        cur.execute("SELECT PRO_NAME, PRO_AVAILABLE_QUANTITY FROM PRODUCTS WHERE PRO_ID = ?", (product_id,))
        pro_name_qun = cur.fetchone()

        if pro_name_qun is None:
            print("Invalid Product ID!")
            return

        pro_name, stock_qty = pro_name_qun

        quantity = int(input(f"Enter quantity of {pro_name} and stock {stock_qty}: "))

        
        if quantity > stock_qty:
            print(f"only {stock_qty} items are avilable in stock.")
            return

        cur.execute("SELECT QUANTITY FROM CART WHERE PRODUCT_ID = ? AND USER_ID = ?", (product_id, current_user_id)) 
        exist = cur.fetchone()

        if exist:
            new_qty = exist[0] + quantity
            cur.execute("UPDATE CART SET QUANTITY = ? WHERE PRODUCT_ID  = ? AND USER_ID = ?", (new_qty, product_id, current_user_id))
        else:
            cur.execute("INSERT INTO CART (USER_ID, PRODUCT_ID, QUANTITY) VALUES (?, ?, ?)", (current_user_id, product_id, quantity))

        con.commit()

        print(f"{pro_name} x {quantity} add to cart successfully...")

    except ValueError as e:
        print("Error:", e)


# ---------------------------------
# view_cart()
# ---------------------------------
def view_cart():

    global current_user_id

    print("\n========== YOUR CART ==========\n")

    cur.execute("""
                SELECT PRODUCTS.PRO_NAME, CART.QUANTITY, PRODUCTS.PRO_PRICE, PRODUCTS.PRO_DISCOUNT
                    FROM CART JOIN PRODUCTS ON CART.PRODUCT_ID = PRODUCTS.PRO_ID WHERE CART.USER_ID = ?
                """, (current_user_id,))
    
    cart_item = cur.fetchall()
    if not cart_item:
        print("Your Cart is empty!")
        return
    
    total = 0

    for name, qty, price, discount in cart_item:
        final_price = price - (price * discount / 100)
        item_total = final_price * qty
        total += item_total

        print(f"{name} | Qty: {qty} | Price after discount: ₹{final_price} | Total: ₹{item_total}")

        
    print("\n--------------------------")
    print(f"Cart Total: ₹{total}")


# ---------------------------------
# checkout()
# ---------------------------------
def checkout():
    global current_user_id

    cur.execute("""
                SELECT SUM((PRO_PRICE - (PRO_PRICE * PRO_DISCOUNT / 100)) * QUANTITY) 
                FROM CART JOIN PRODUCTS ON CART.PRODUCT_ID = PRODUCTS.PRO_ID WHERE CART.USER_ID = ?
                """, (current_user_id,))
    
    total = cur.fetchone()[0]

    if total is None:
        print("Cart is empty! Add products before checkout.")
        return
    
    phone = input("Enter delivery phone (10 digits): ")
    phone_pattern = r"^\d{10}$"
    
    if not re.match(phone_pattern, phone):
        print("Contact number is must be 10 number.")
        return

    address = input("Enter delivery address: ")

    cur.execute("""
        INSERT INTO ORDERS (USER_ID, DELIVERY_PHONE, DELIVERY_ADDRESS, TOTAL_AMOUNT)
        VALUES (?, ?, ?, ?)
        """, (current_user_id, phone, address, total))
    
    # Fetch all cart items
    cur.execute("SELECT PRODUCT_ID, QUANTITY FROM CART WHERE USER_ID = ?", (current_user_id,))
    items = cur.fetchall()

    # Reduce product stock safely
    for pid, qty in items:
        cur.execute("""
            UPDATE PRODUCTS
            SET PRO_AVAILABLE_QUANTITY = PRO_AVAILABLE_QUANTITY - ?
            WHERE PRO_ID = ?
        """, (qty, pid))
        
    
    # Clear Cart
    con.commit()
    print(f"Order placed successfully! Total Amount: ₹{total}")










# ---------------------------------
# Main Menu
# ---------------------------------
current_user_id = None
while True:
    try:
        print("\n=== Welcome to DMart Grocery Store ===\n")

        if current_user_id is None:
            print("1. SIGN UP")
            print("2. LOG IN")
            print("3. EXIT")
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                sign_up()
            elif choice == 2:
                current_user_id = login()
            elif choice == 3:
                print("Thank you for visiting DMart!")
                break
            else:
                print("Invalid choice! Try again.")
        else:       
            print("1. VIEW PRODUCTS")
            print("2. ADD PRODUCTS TO CART")
            print("3. VIEW CART")
            print("4. PLACE ORDER (CHECKOUT)")
            print("5. LOG OUT")

            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_products()
            elif choice == 2:
                add_to_cart()
            elif choice == 3:
                view_cart()
            elif choice == 4:
                checkout()
            elif choice == 5:
                print("Thank you for shopping at GROCERY_STORE! \nLoged out successfully!")
                current_user_id = None
            else:
                print("Invalid choice! Please try again.")
    except Exception as e:
        print(e)
