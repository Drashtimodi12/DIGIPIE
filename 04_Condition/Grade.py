# Input marks and print grade:
# 90–100 → A
# 80–89 → B
# 70–79 → C
# 50–69 → D
# below 50 → Fail

a = float(input("Enter your Grade: "))
if a >= 90:
    print("A grade")
elif a >= 80:
    print("B grade.")
elif a >= 70:
    print("C grade.")
elif a >= 50:
    print("D grade.")
else:
    print("Fail")