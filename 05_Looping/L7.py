# Input a number and calculate:
# Total digits
# Sum of digits using a loop

num = input("Enter digits: ")
total_digigts = 0
sum_num = 0


for i in num:
    total_digigts += 1
    sum_num += int(i)
    
print("Total number: ", total_digigts)
print("Sum of Digits: ", sum_num)
