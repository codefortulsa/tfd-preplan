# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from streetaddress import StreetAddressParser

from .utils import normalize_street_type


class AddressForm(forms.Form):
    street_no = forms.IntegerField(min_value=0)
    street_dir = forms.RegexField(regex=r'^[NORnorSOUsouTHthEAeaWEweSTst]+$', min_length=1, error_message="Not a valid direction, check your spelling.")
    street_name = forms.RegexField(regex=r'^[\w+ \'&\.]+', min_length=1, error_message="Not a valid street name.  Check for special characters.")
    street_type = forms.RegexField(regex=r'^[\w+]+', min_length=1, error_message="Not a valid street type.  Check for special characters.")


    def clean_address(self):
        self.cleaned_data['address'] = "%d %s %s %s".format(self.cleaned_data['street_no'], self.cleaned_data['street_dir'], self.cleaned_data['street_name'], self.cleaned_data['street_type'])

        parser = StreetAddressParser()
        parts = parser.parse(self.cleaned_data['address'])
        street_dir, street_name = parts['street_name'].split(' ', 1)
        self.cleaned_data['street_no'] = parts['house']
        self.cleaned_data['street_dir'] = street_dir
        self.cleaned_data['street_name'] = street_name
        self.cleaned_data['street_type'] = normalize_street_type(parts['street_type'])
        return self.cleaned_data['address']
