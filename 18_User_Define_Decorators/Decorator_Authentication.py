# Authentication Decorator


def greet(fun):
    def wrapper():
        print("-----START-----")
        a = input("Enter Name: ").upper()
        if a == "ADMIN":
            fun(a)
        else:
            print("Acces Denied...")
        print("-----END-----\n")
    return wrapper


@greet
def dashboard(a):
    print(f"Welcome {a}...")
    

dashboard()