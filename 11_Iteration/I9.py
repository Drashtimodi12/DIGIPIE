# Flatten a 2D list using iteration (without using sum or itertools).
list2D = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for sub_item in list2D:
    for item in sub_item:
        flat_list.append(item)
print(flat_list)
