# Match only strings that contain exactly 3 digits.
# Example inputs:
# 123 → ✔
# 45 → ✘
# 1234 → ✘

import re


pattern = r"^\d{3}$"
mystr = '123'
result = re.match(pattern, mystr)
if result:
    print("Match Sucessfully: ", result)
else:
    print("Not match.")

print("\n\n========================================")

# Match a string that contains only uppercase alphabets.
# Examples:
# HELLO ✔
# HELLO123 ✘

pattern = r"^[A-Z]+$"
mystr = "HELLO"
res = re.match(pattern, mystr)
print(res)

print("\n\n========================================")

# Match lowercase letters only (at least 1 letter).
# Example:
# hello → ✔
# Hello123 → ✘

pattern = r"[a-z]+"
mystr = "hello"
res = re.match(pattern, mystr)
print(res.group())

print("\n\n========================================")

# Match a string that starts with a digit and ends with a letter.
# Examples:
# 1a → ✔
# 9helloZ → 🟨 (ends with uppercase → depends, you decide)
# abc1 → ✘

pattern = r"^\d+[A-Za-z]+$"
mystr =  "9helloZ"
res = re.match(pattern, mystr)
print(res)

