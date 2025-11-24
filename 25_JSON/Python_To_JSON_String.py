"""
json.dumps()
    dumps = “dump to string”
    It converts Python object → JSON string

When do we use json.dumps()?
    Sending data through API
    Storing JSON in a file
    Logging/outputting JSON
    Converting Python objects for network transfer

    Parameter	            Meaning
    indent	            pretty formatting
    sort_keys	        sorts keys alphabetically
    ensure_ascii=False	allows Hindi, Gujarati, emojis, non-English text
    skipkeys=True	    ignores invalid keys
    default	handle      custom objects
"""

import json

data = {"name": "Drashti", "age": 22, "skills": ["Python", "Django"]}
print("Data format is ", type(data))    # OP: Data format is  <class 'dict'>
json_str = json.dumps(data)
print(json_str)         # OP: {"name": "Drashti", "age": 22, "skills": ["Python", "Django"]}
