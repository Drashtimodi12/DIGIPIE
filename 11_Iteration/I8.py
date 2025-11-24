# Iterate through a list of lists (nested list) and print all items.

list1 = [1, 2, 3, 6, [2, 6, 8], 9]

for i in list1:
    if isinstance(i, list):
        for sub in i:
            print(sub, end=" ")
    else:
        print(i, end = " ") 