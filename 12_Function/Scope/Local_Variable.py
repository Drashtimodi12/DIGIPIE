a = 20      # Global Variable

def test() :
    a = 50      # Local Variable
    a += 20
    print(a)        # Output: 70 (local scope)

print("Before: ", a)        # Output: before: 20 (global scope)
test()                      # Output: 70 Local variable 'a' inside test() does not affect the global 'a'
print("After: ", a)         # Output: after: 20 (global scope)
