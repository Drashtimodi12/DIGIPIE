# Match an Indian phone number (10 digits).
# Examples:
# 9876543210 ✔
# 09876543210 ✘ (11 digits)
# 98765-43210 ✘

import re

pattern = r"^\+91-\d{10}$"
mystr = "+91-9909449049"
res = re.match(pattern, mystr)
print(res)
