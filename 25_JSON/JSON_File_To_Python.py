"""
json.load()
    load = read JSON from a file
    json.load() is used to read JSON file → Python object.

When do we use json.load()?
    Reading data from a JSON file
    Loading settings/config files
    Reading saved user data
    Importing JSON for processing

Parameter	        Use
object_hook	    modify decoded dict
parse_int	    customize integer parsing
parse_float	    customize float parsing
strict=False	allow trailing commas
"""

# Read JSON file into Python dict
import json

with open('Python_To_JSON_File.json', 'r') as f:
    data = json.load(f)
print("Read JSON file into Python dict", data)     
# OP: Read JSON file into Python dict {'name': 'Drashti', 'age': 22}




# Reading JSON list from file
with open('JSON_File_To_Python.json') as f:
    data = json.load(f)
print("Reading JSON list from file", data)        
# op: Reading JSON list from file [10, 20, 30, 40]