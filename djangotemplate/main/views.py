from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
