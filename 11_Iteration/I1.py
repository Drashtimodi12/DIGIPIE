# Iterate through a list of numbers and print each element.
# Manually iterate through a list using iter() and next().

mylist = [1, 3, 5, 7]

it = iter(mylist)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


print("\n\n======================\n")
# Use enumerate() to print index and element of a list.
mylist = [9, 8, 7, 6, 5]
for i, a in enumerate(mylist, start=1):
    print(i, ":", a)



print("\n\n======================\n")
# Use a for loop to print numbers from 1 to 10.
for i in range(1, 11):
    print(i, end = " ")



print("\n\n======================\n")
# Use a for loop to find the largest number in a list.
mylist = [9, 8, 7, 6, 5]
larg = mylist[0]
for i in mylist:
    if i > larg:
        larg = i
print(larg)


print("\n\n======================\n")
# Iterate through a list and separate even and odd numbers into two lists.
list8 = [9, 8, 7, 6, 5]
even_list = []
odd_list = []
for i in list8:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even Numbers = ", even_list)
print("Odd Numbers = ", odd_list)