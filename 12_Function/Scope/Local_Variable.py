
# 11. Function with Local Variable
a = 10
def sum(a, b):
    sum = a + b
    return sum
result = sum(5, 10)
print(f"The sum is {result}.")
# Output: The sum is 15.

print("\n============================\n")

# Local → accessible only inside that function

a = 20      # Global Variable

def test() :
    a = 50      # Local Variable
    a += 20
    print(a)        # Output: 70 (local scope)

print("Before: ", a)        # Output: before: 20 (global scope)
test()                      # Output: 70 Local variable 'a' inside test() does not affect the global 'a'
print("After: ", a)         # Output: after: 20 (global scope)

