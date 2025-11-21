class A:

    def __init__(self):
        self.__salary = 3000   # Private attribute (Name Mangling: _A__salary)

a = A()

print(a.__salary)   # ❌ ERROR: Cannot access private attribute directly
