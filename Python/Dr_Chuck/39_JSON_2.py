# Import the json module to work with JSON data
import json

# Define a JSON string with an array of objects
input = '''[
    {"id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    {"id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
]'''

# Summary of Differences
# {}: Represents a single object (dictionary) with key-value pairs.

# []: Represents an array (list) of values, which can include 
# objects, arrays, or primitive values.


# Parse the JSON string into a Python 'list of dictionaries'
info = json.loads(input)

# Print the number of items in the list
print('User count:', len(info))

# Iterate over each dictionary in the list
for item in info:
    # Print the value associated with the "name" key
    print('Name:', item['name'])
    # Print the value associated with the "id" key
    print('ID:', item['id'])
    # Print the value associated with the "x" key
    print('Attribute:', item['x'])


