"""
json.loads()
    loads = “load from string”
    It converts JSON string → Python object

When do we use json.loads()?
    Reading API response
    Reading JSON from database
    Parsing JSON strings
    Converting JSON input to Python for processing

Parameter	        Meaning
object_hook	    modify dictionary after loading
parse_int	    custom function to parse integers
parse_float	    custom function for floats
strict=False	allows trailing commas      
"""

# Convert JSON → Python

import json

# Use json.loads() ONLY when the input is a string
json_str = '{"name": "Drashti", "age": 22, "skills": ["Python", "Django"]}'
print("JSON String is ", type(json_str))    # OP: JSON String is  <class 'str'>
data = json.loads(json_str) 
print(data["name"], data["skills"][0])      # OP: Drashti Python
print(data)         # OP: {'name': 'Drashti', 'age': 22}

