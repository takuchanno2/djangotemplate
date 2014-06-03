# coding:utf-8

from django.contrib.auth.forms import AuthenticationForm
from core import settings

def project_name(request):
    return {
            "project_name": settings.PROJECT_NAME,
    }

