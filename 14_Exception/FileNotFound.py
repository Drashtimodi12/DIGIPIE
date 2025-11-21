try:
    with open('F1.txt', 'r') as f:
        f.read()

except FileNotFoundError as e:
    print(e)

finally:
    print("Finally Block Executed. ")
