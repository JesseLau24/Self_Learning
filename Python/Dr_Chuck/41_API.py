# Import necessary libraries
import urllib.request, urllib.parse, urllib.error
import json

# Base URL for the Google Geocoding API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    # Prompt the user for a location
    address = input('Enter location: ')
    if len(address) < 1: 
        break  # Exit loop if no input

    # Construct the URL with the user-provided address
    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)  # Print the URL being retrieved
    uh = urllib.request.urlopen(url)  # Open the URL
    data = uh.read().decode()  # Read and decode the response
    print('Retrieved', len(data), 'characters')  # Print the length of the response

    # Attempt to parse the JSON data
    try:
        js = json.loads(data)
    except json.JSONDecodeError:
        js = None
        print('Failed to parse JSON data')

    # Check if the response was successful
    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve ===')
        print(data)  # Print the raw data for debugging
        continue  # Continue to the next iteration

    # Access and print latitude, longitude, and formatted address
    if "results" in js and len(js["results"]) > 0:
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print('Latitude:', lat, 'Longitude:', lng)
        location = js["results"][0]["formatted_address"]
        print('Location:', location)
    else:
        print('No results found')
