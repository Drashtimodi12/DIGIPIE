# Print your name decorator task


def greet(fun):
    def start():
        print("-----START-----")
        fun()
        print("-----END-----\n")
    return start

@greet
def hello():
    print("HEllO")

@greet
def greet():
    n = input("Enter your name: ")
    print(f"Wellcome {n}.")


hello()

print("\n=====================\n")

greet()


# OP:
# -----START-----
# HEllO
# -----END-----

# =====================

# -----START-----
# Enter your name: Drashti
# Wellcome Drashti.
# -----END-----