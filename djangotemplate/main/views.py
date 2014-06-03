from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class TopPageView(TemplateView):
    template_name = "main/top.html"

    def get_context_data(self, **kwargs):
        context = super(TopPageView, self).get_context_data(**kwargs)
        return context
