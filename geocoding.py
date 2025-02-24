import googlemaps
from datetime import datetime
import pprint

gmaps = googlemaps.Client(key='AIzaSyBFMR8WXvhXfkDGMy7QQ8LvgZJaP6Ovp2Y')

location_search = input("Enter location name: ")

# Geocoding an address
geocode_result = gmaps.geocode(location_search)
nav_points = geocode_result[0]['navigation_points'][0]
google_latitude = nav_points['location']['latitude']
google_longitude = nav_points['location']['longitude']
print(google_latitude)
print(google_longitude)

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

'''
# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)

# Get an Address Descriptor of a location in the reverse geocoding response
address_descriptor_result = gmaps.reverse_geocode((40.714224, -73.961452), enable_address_descriptor=True)
'''
