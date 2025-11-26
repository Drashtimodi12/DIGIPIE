student = {"name": "Drashti", "age": 21, "city": "Surat"}

# Print keys
print(student.keys())
print("------------------------")

# Print values
print(student.values())
print("------------------------")

# Change city → Ahmedabad
student.update(city='Ahmedabad')
print(student.items())
print("------------------------")

# Add new key: "degree": "B.Tech"
student.update(degree = 'B.Tech')
print(student.items())
print("------------------------")

# Remove "age"
student.pop('age')
print(student.items())