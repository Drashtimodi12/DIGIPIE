# Bitwise Operators:  & , | , ^ , << , >> , ~


# Perform bitwise AND, OR, XOR on two numbers.
x = 10   # 1010 in binary
y = 5    # 0101 in binary

print("Bitwise AND (x & y):", x & y)
print("Bitwise OR  (x | y):", x | y)
print("Bitwise XOR (x ^ y):", x ^ y)


print("\n===========================\n")

# Shift a number left by 2 bits.
print("Left Shift:", x << 2)

print("\n===========================\n")

# Convert a number to binary, then apply bitwise NOT.
binary = bin(x)
result = ~x
not_binary = bin(result)

print("Original Number:", x)
print("Binary:", binary)
print("Bitwise NOT (~n):", result)      # ~n  =  -(n + 1)
print("Binary of NOT:", not_binary)