from django.views.generic import FormView, TemplateView
from django.conf import settings

from .forms import AddressForm
from .utils import get_property_data
from urllib import urlencode

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


        coordinates = getCoordinates(form.cleaned_data['address'])
        import ipdb; ipdb.set_trace()

        return self.render_to_response(
            self.get_context_data(
                form=form, property=data, coordinates=coordinates
            )
        )
