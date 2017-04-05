from django.views.generic import FormView, TemplateView
from django.conf import settings
from django.http import HttpResponse
from django.views import View

from .forms import AddressForm
from .utils import get_property_data
from urllib import urlencode

from settings import GOOGLE_KEY

from  .tfd_geocoder import getCoordinates

class Home(TemplateView):
    template_name = 'home.html'


class AddressLookupView(FormView):
    template_name = 'address_lookup.html'
    form_class = AddressForm

    def form_valid(self, form):
        form.clean_address()
        data = get_property_data(
            form.cleaned_data['street_no'], form.cleaned_data['street_dir'],
            form.cleaned_data['street_name'], form.cleaned_data['street_type'])

        address = form.cleaned_data['address']
        coords = getCoordinates(address)
        return self.render_to_response(
            self.get_context_data(
                form=form, property=data,
                coordinates=coords,
                address = address,
                GOOGLE_KEY=GOOGLE_KEY
            )
        )

# This view works but is not used
class StreetMap (View):
    def get(self, request, *args, **kwargs):
        street_address=self.kwargs['address']
        mapHTML = getSlippyMap(street_address)
        return HttpResponse(mapHTML)
