from django.views.generic import TemplateView
from django.conf import settings

class Home(TemplateView):
    template_name = 'home.html'
