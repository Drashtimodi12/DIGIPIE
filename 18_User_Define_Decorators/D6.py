# Task 13: Create a class ShoppingCart with:
# instance attribute: items (list)
# methods:
# add_item(item)
# remove_item(item)
# view_cart()
# empty_cart()
# Create an object → add items → remove one → display final cart.


class ShoppingCart:

    def __init__(self):
        self.items = []         # items will store list of products
    
    def add_item(self):
        a = input("\nAdd Shooping item in Cart: ").upper()
        self.items.append(a)
        print(f"'{a}' add in cart.")

    def remove_item(self):
        b = input("\nEnter Product to remove from Cart: ").upper()
        if b in self.items:
            self.items.remove(b)
            print(f"'{b}' remove form Cart.")
        else:
            print(f"'{b}' Not found in Cart.")

    def view_cart(self):
        if len(self.items) == 0:
            print("\nYour Cart is Empty.")
        else:
            print("Items in Cart is: ")
            for i in self.items:
                print(i, end = ', ')
        
    def empty_cart(self):
        self.items.clear()
        print("\n\nCart has been Empty...")

sc = ShoppingCart()
sc.add_item()
sc.add_item()
sc.add_item()

sc.remove_item()
sc.view_cart()
sc.empty_cart()

# OP:
# Add Shooping item in Cart: milk
# 'MILK' add in cart.

# Add Shooping item in Cart: apple
# 'APPLE' add in cart.

# Add Shooping item in Cart: banana
# 'BANANA' add in cart.

# Enter Product to remove from Cart: milk
# 'MILK' remove form Cart.
# Items in Cart is:
# APPLE, BANANA,

# Cart has been Empty...