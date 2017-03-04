# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from streetaddress import StreetAddressParser

from .utils import normalize_street_type


class AddressForm(forms.Form):
    address = forms.CharField(max_length=255)

    def clean_address(self):
        parser = StreetAddressParser()
        parts = parser.parse(self.cleaned_data['address'])
        street_dir, street_name = parts['street_name'].split(' ', 1)
        self.cleaned_data['street_no'] = parts['house']
        self.cleaned_data['street_dir'] = street_dir
        self.cleaned_data['street_name'] = street_name
        self.cleaned_data['street_type'] = normalize_street_type(parts['street_type'])
        return self.cleaned_data['address']

