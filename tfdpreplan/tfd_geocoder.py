from mapbox import Geocoder
from settings import MAPBOX_TOKEN

geocoder = Geocoder(access_token=MAPBOX_TOKEN)

def getCoordinates(steet_address):

    response = geocoder.forward(steet_address)

    first = response.geojson()['features'][0]

    return first['geometry']['coordinates']
