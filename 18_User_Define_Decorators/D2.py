# Function task — Reverse a string

def greet(fun):
    # Decorator function
    def start():
        print("WELCOME")

        # Take input inside decorator
        a = input("Enter any string to reverse: ")

        # Reverse the string
        reversed_string = a[::-1]

        # Call original function with reversed string
        fun(reversed_string)

        print("Thank you")
    return start


@greet
def st(result):
    # This function only prints the reversed string
    print("Reversed string:", result)


# Call the function
st()

# OP:
# WELCOME
# Enter any string to reverse: modi
# Reversed string: idom
# Thank you