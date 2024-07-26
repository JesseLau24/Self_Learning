import urllib.request, urllib.parse, urllib.error
import json

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY' # doesn't work if you don't have API key.
serviceurl = f'http://maps.googleapis.com/maps/api/geocode/json?key={api_key}&'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except json.JSONDecodeError:
        js = None
        print('Failed to parse JSON data')

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve ===')
        print(data)
        continue

    if "results" in js and len(js["results"]) > 0:
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print('Latitude:', lat, 'Longitude:', lng)
        location = js["results"][0]["formatted_address"]
        print('Location:', location)
    else:
        print('No results found')

