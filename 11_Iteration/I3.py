# Print all even numbers from a list using a loop.

mylist = [1, 2, 3, 4, 5, 6]
for i in mylist:
    if i % 2 == 0:
        print(i, end = " ")
    else:
        pass



print("\n\n======================\n")

# Iterate through a list and create a new list containing only positive numbers.

mylist = [1, -4, 2, 4, 6.4, -9]
positive_list = []

for i in mylist:
    if i > 0:
        positive_list.append(i)
print(positive_list)