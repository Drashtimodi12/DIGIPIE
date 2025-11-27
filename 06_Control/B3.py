# Nested Loops with Break
# Print a multiplication table (1 to 10) for a number.
# Stop the inner loop if the product is greater than 30 using break.

for table in range(1, 11):
    for i in range(1, 11):
        product = table * i 
        if product > 30:
            break
        print(f"{table} * {i} = {table * i}")
    print()