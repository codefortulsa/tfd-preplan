import HTMLParser
import requests

from mapbox import Geocoder
from settings import MAPBOX_TOKEN

geocoder = Geocoder(access_token=MAPBOX_TOKEN)

mapbox_url = "https://api.mapbox.com/v4"

def getCoordinates(steet_address):

    response = geocoder.forward(steet_address)

    first = response.geojson()['features'][0]

    return first['geometry']['coordinates']


def getSlippyMap(street_address):
    map_id = 'mapbox.light'
    options = 'zoomwheel,zoompan'
    zoom = 15
    coords = getCoordinates(street_address)
    # hash #{zoom}/{lat}/{lon}
    hash = '%s/%s/%s' % (zoom, coords[1],coords[0])
    request_url = '%s/%s/%s.html?access_token=%s&#%s' % (
        mapbox_url, map_id, options, MAPBOX_TOKEN, hash
    )
    map_html = requests.get(request_url)
    return map_html.text
