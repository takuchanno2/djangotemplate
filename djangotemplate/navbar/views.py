from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class NavbarExampleView(TemplateView):
    template_name = "navbar/example.html"

    def get_context_data(self, **kwargs):
        context = super(NavbarExampleView, self).get_context_data(**kwargs)
        return context
