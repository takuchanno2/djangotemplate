# coding:utf-8

from django.contrib.auth.forms import AuthenticationForm
from core import settings

def app_name(request):
    return {
            "app_name": settings.APP_NAME,
    }

