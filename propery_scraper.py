import requests


def get_property_data(street_no, street_dir, street_name, street_type):
    source_url = 'http://www.assessor.tulsacounty.org/assessor-property-view.php'
    data = {
        'streetno': street_no,
        'predirection': street_dir,
        'streetname': street_name,
        'streettype': sanitize_street_type(street_type),
        'subaddr': 'Search+by+address',
        'accepted': 'accepted',
    }

    return requests.post(source_url, data=data)


def sanitize_street_type(street_type):
    types = {
        'AV': ['ave', 'avenue'],
        'BV': ['blvd', 'boulevard'],
        'CR': ['cir', 'circle'],
        'CT': ['crt', 'court'],
        'DR': ['dr', 'drive'],
        'E': ['e', 'east'],
        'EX': ['expy', 'expw', 'expressway'],
        'HY': ['hw', 'highway'],
        'LN': ['ln', 'lane'],
        'N': ['n', 'north'],
        'PK': ['pk', 'park'],
        'PL': ['pl', 'place'],
        'RD': ['rd', 'road'],
        'S': ['s', 'south'],
        'ST': ['st', 'street'],
        'TE': ['terr', 'terrace'],
        'TL': ['tr', 'trail'],
        'WY': ['way'],
        'W': ['w', 'west'],
    }

    street_type = street_type.upper()
    if street_type not in types:
        for st, choices in types.items():
            if street_type.lower() in choices:
                street_type = st
                break
    return street_type
