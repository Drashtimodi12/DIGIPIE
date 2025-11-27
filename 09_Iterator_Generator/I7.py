# Iterate through a string and print each character.
st = "I am Drashti"
for i in st:
    print(i, end = " ")


print("\n\n======================\n")
# Iterate through a string and count vowels, consonants, digits, and spaces.
st1 = "I am Drashti 123."

vowels = 'aeiouAEIOU'
vowels_count = 0
consonanta_count = 0
digits_count = 0
spaces_count = 0

for ch in st1:
    if ch in vowels:
        vowels_count += 1
    elif ch.isalpha():
        consonanta_count += 1
    elif ch.isdigit():
        digits_count += 1
    elif ch == " ":
        spaces_count += 1

print("Vowels: ", vowels_count)
print("Consonanta: ", consonanta_count)
print("Digits: ", digits_count)
print("Space: ", spaces_count)
