"""
What is Random Module?
Python provide multiple inbuilt function that are used to choose or generate random number by 
using random module.

Random number Operations:-
Choice(): choice() is inbuilt function of random module, which is used to return random number from list, tuple, set.
Randint(): randint() is inbuilt function of random module, which is used to generate random number from particular given range.
Shuffle(): shuffle() is inbuilt function of random module, which is used to shuffle a value of list.

from random import functionname     or
import random
"""


# -----1. choice() ------
from random import choice
l = [1, 4, 6, 3, 9, 10]
print(choice(l))
# Output: 6

# -----2. randint() ------
from random import randint
otp = randint(100000, 999999)
print("OTP is: ", otp)
# Output: 302646

# ----3. shuffle() ------
from random import shuffle
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
shuffle(a)
print("Shuffle list: ", a)
# Output: Shuffle list:  [0, 4, 5, 1, 7, 2, 8, 3, 9, 6]