# JSON is short for 'JavaScript Object Notation' (you can read about JSON at http://www.json.org/)

# Import the json module to work with JSON data
import json

# Define a JSON string with data about a person
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

# Parse the JSON string into a Python dictionary
info = json.loads(data)

# Print the value associated with the "name" key in the dictionary
print('Name:', info["name"])

# Print the value associated with the "hide" key within the "email" 
# dictionary in the main dictionary
print('Hide:', info["email"]["hide"])






