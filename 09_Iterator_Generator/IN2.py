# Q3. Given a list of words, return a new list containing words whose length is greater than 5.
l = ['apple', 'banana', 'kiwi']
a = [i for i in l if len(i) > 5]
print(a)
# OP: ['banana']

print("\n=====================\n")

# Q4. Convert all words in a list to uppercase using list comprehension.
mylist = ['apple', 'banana', 'kiwi']
a = [i.upper() for i in mylist]
print(a)
# OP: ['APPLE', 'BANANA', 'KIWI']

print("\n=====================\n")

# Q6. From a sentence, generate a list of vowels only using list comprehension.
a = "my name is drashti"
re = [i for i in a if i in 'aeiouAEIOU']
print(re)