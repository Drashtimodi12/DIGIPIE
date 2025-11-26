a = 10
print(f"{a} data type is {type(a)}")
print("------------------------")

b = 12.5
print(f"{b} data type is {type(b)}")
print("------------------------")

c = "Drashti"
print(f"{c} data type is {type(c)}")
print("------------------------")

d = True
print(f"{d} data type is {type(d)}")
print("------------------------")

e = None
print(f"{e} data type is {type(e)}")
print("------------------------")

f1 = [1, 2, 3]
print(f"{f1} data type is {type(f1)}")
f2 = list((2, 5, 2))
print(f"{f2} data type is {type(f2)}")
print("------------------------")

g1 = (4, 5)
print(f"{g1} data type is {type(g1)}")
g2 = tuple((2, 4, 2))
print(f"{g2} data type is {type(g2)}")
print("------------------------")

h1 = {6, 7}
print(f"{h1} data type is {type(h1)}")
h2 = set((True, 2, 6))
print(f"{h2} data type is {type(h2)}")
print("------------------------")

i1 = {"name": "Modi"}
print(f"{i1} data type is {type(i1)}")
i2 = dict(name = "Modi")
print(f"{i2} data type is {type(i2)}")

print("------------------------")



# Accept input and print datatype
# Take input from user and print:
# value entered
# its datatype

a = input("Enter something: ")
print(f"User input is {a} and there datatype is {type(a)}.")

print("------------------------")



# Find datatype of each key and value

d = {"name": "Drashti", "age": 21, "marks": 88.5}


for k, v in d.items():    
    print(f"Key : {k} -> {type(k).__name__}, Value : {v} -> {type(v).__name__}")
