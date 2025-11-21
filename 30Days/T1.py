# Print your name 5 times

# name = 'Drashti' 
# for i in range(1, 6):
#     print(i, name)


# name = 'Drashti'
# i = 1
# while i <= 5:
#     print(name)
#     i += 1


# name = 'Drashti'
# print(name * 5)



def print_name(a):
    if a == 0:
        return 0
    else:
        print('Drashti')
        print_name(a-1)
print_name(5)