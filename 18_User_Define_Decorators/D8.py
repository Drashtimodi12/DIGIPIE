# Q28. Write a decorator that runs a function only if the user is logged in 
# (simulate with variable is_login = True).

is_login = True

def login_required(func):
    def wrapper(*args, **kwargs):
        if is_login:                 
            return func(*args, **kwargs)   
        else:
            print("Access Denied! Please login first.")
    return wrapper


@login_required
def dashboard(active):
    if active:
        print("Welcome to your dashboard!")
    else:
        print("Dashboard is inactive.")


dashboard(True)
# OP: Welcome to your dashboard!

print("\n===========================\n")

dashboard(False)
# OP: Dashboard is inactive.
