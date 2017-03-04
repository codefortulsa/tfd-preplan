import re

import requests
from pyquery import PyQuery


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

    resp = requests.post(source_url, data=data)
    data = parse_markup(resp.content)
    return data


def parse_markup(content):
    data = {
        'improvements': [],
        'images': [],
    }
    d = PyQuery(content)
    rows = d('#quick table tr, #general table tr')
    for row in rows:
        cells = row.findall('td')
        key = sanitize_data_key(cells[0].text)
        data[key] = cells[1].text
    headers = []
    for num, row in enumerate(d('#improvements table tr')):
        if num == 0:
            headers = [sanitize_data_key(c.text) for c in row.findall('th')]
        else:
            cells = row.findall('td')
            data_row = {}
            for i, cell in enumerate(cells):
                data_row[headers[i]] = cell.text
            data['improvements'].append(data_row)
    data['images'] = [i.attrib['src'] for i in d('#images table img')]
    return data


def sanitize_data_key(key):
    key = key.lower()
    key = re.sub(r'[^a-z0-9_]', '_', key)
    key = re.sub(r'_+', '_', key)
    key = re.sub(r'^_|_$', '', key)
    return key


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
