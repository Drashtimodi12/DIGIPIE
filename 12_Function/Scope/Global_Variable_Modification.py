# Create a global variable count = 0, and a function that increases it by 1 each time it’s called.

# count = 0 
# def inc():
#     global count
#     count += 1
#     print(f"number is: {count}")
# inc()
# inc()



# global Keyword → Needed if you want to modify a global variable inside a function.
a = 20      # Global Variable

def test() :
    global a       # Accessing the global variable
    a = 50         # Modifying global variable
    a += 20
    print(a)        # Output: 70 (modifies global a)

print("Before: ", a)        # Output: before: 20
test()                      # Output: 70
print("After: ", a)         # Output: after: 70
   