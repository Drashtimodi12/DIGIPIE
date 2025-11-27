# Use zip() to iterate over two lists at the same time.

mylist1 = [1, 4, 6, 2, 7]
mylist2 = [23, 65, 1, 9, 0]

for x, y in zip(mylist1, mylist2):
    print(x, y)



print("\n\n======================\n")
# Iterate backwards through a list using a loop.
mylist = [1, 4, 6, 2, 7]
for i in mylist[::-1]:
    print(i, end = " ")


print("\n\n======================\n")
# Iterate through a list and count how many times each element appears.
mylist = [1, 4, 6, 2, 7, 4, 1, 2, 4]
count_dict = {}
for item in mylist:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict)


