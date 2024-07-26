import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://nominatim.openstreetmap.org/search?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'q': address, 'format': 'json'})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except json.JSONDecodeError:
        js = None
        print('Failed to parse JSON data')

    if not js:
        print('=== Failure To Retrieve ===')
        print(data)
        continue

    if len(js) > 0:
        lat = js[0]["lat"]
        lon = js[0]["lon"]
        print('Latitude:', lat, 'Longitude:', lon)
        display_name = js[0]["display_name"]
        print('Location:', display_name)
    else:
        print('No results found')
