import urllib.request, urllib.parse, urllib.error
import json

# Base URL for the OpenStreetMap Nominatim search API
serviceurl = 'https://nominatim.openstreetmap.org/search?'

while True:
    # Prompt the user to enter a location
    address = input('Enter location: ')
    
    # If the user enters a blank input, break out of the loop
    if len(address) < 1:
        break

    # Build the URL by appending the query parameters to the base URL
    url = serviceurl + urllib.parse.urlencode({'q': address, 'format': 'json'})

    # Print the URL that is being retrieved
    print('Retrieving', url)
    
    # Open the URL and read the response
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    
    # Print the number of characters retrieved
    print('Retrieved', len(data), 'characters')

    try:
        # Parse the JSON response
        js = json.loads(data)
    except json.JSONDecodeError:
        # If JSON parsing fails, set js to None and print an error message
        js = None
        print('Failed to parse JSON data')

    # If js is None or empty, print an error message and continue the loop
    if not js:
        print('=== Failure To Retrieve ===')
        print(data)
        continue

    # If there are results in the JSON response
    if len(js) > 0:
        # Extract the latitude and longitude of the first result
        lat = js[0]["lat"]
        lon = js[0]["lon"]
        print('Latitude:', lat, 'Longitude:', lon)
        
        # Extract the display name of the first result
        display_name = js[0]["display_name"]
        print('Location:', display_name)
    else:
        # If no results were found, print a message
        print('No results found')
