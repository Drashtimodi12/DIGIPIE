"""What is Function in Python?
A function is a block of code which only runs when it is called. 
It also helps to reuse the code. It starts with the keyword 'def' followed by the function name and parentheses ().
You can pass data, known as parameters, into a function.

Types of Functions in Python:
1. Built-in Functions   -> print(), input(), len(), type(), range(), round(), etc.
2. User-defined Functions
3. Anonymous Functions (Lambda Functions) 
4. Recursive Functions
"""


# -----------In Built Functions-----------

print("hello".title())      # Hello

for i in range(1, 6):
    print(i)
    # 1
    # 2
    # 3
    # 4
    # 5

a = round(32.4443, 2)
print(a)    # 32.44


# -----------User Defined Functions-----------

# 1. Function without argument and without return type
def myfun1():
    print("This is my first function.")
myfun1()
# Output: This is my first function.

# 2. Function with one argument and without return type
def myfun2(name):
    print(f"Hello, {name}!")
myfun2("Drashti")
# Output: Hello, Drashti!

# 3. Function with multiple arguments and without return type
def myfun3(a, b, c):
    sum = a + b + c
    print(f"The sum of {a}, {b}, {c} is {sum}.")
myfun3(5, 10, 1)
# Output: The sum of 5, 10, 1 is 16.

# 4. Function with keyword arguments
def myfun4(name, age, city):
    print("Address Details: ", city)
    print(f"My name is {name}. I am {age}. i am leave in {city}.")

myfun4(age=25, name="Drashti", city="Ahmedabad")
# Output: Address Details: Drashti
#         My name is Drashti. I am 25. i am leave in Ahmedabad.

# 5. Function with default arguments
def myfun5(name='Drashti', age=25):
    print(f"My name is {name}. I am {age} years old.")
myfun5()
myfun5("Anjli", 24)
# Output: My name is Drashti. I am 25 years old.
#         My name is Anjli. I am 24 years old.

# 6. Passing list in function
def myfun6(fruits):
    for i in fruits:
        print(i)
f = ['Mango', 'Apple', 'Banana']
myfun6(f)
# Output: Mango
#         Apple
#         Banana

# 7. Function with return value
def myfun7(a):
    return 2 * a
result = myfun7(5)
print(f"The result is {result}.")  
# Output: The result is 10.

# 8. Recursive Function (Function calling itself)
def myfun8(n):
    if n <= 1:
        return 1
    else:
        return n + myfun8(n - 1)
print("The sum is", myfun8(5))
# Output: The sum is 15

# 9. Lambda Function (Anonymous Function)
a = lambda x: x + 5
print(a(10))
# Output: 15

a = lambda x, y : x * y
print(a(5, 6))
# Output: 30


# 10. Function with Global
x = 12
def myfun9():
    global x
    print("Value of x inside function:", x)  
    x = 15
myfun9()
print("Value of x outside function:", x)     # variable x is global variable, so it can be accessed outside the function
# Output: Value of x inside function: 12
#         Value of x outside function: 15

# 11. Function with Local Variable
def sum(a, b):
    sum = a + b
    return sum
result = sum(5, 10)
print(f"The sum is {result}.")
print(a)    # variable a is local variable, so it will give error if we try to print it outside the function
# Output: The sum is 15.
#         <function <lambda> at 0x0000020AF176DF80>

