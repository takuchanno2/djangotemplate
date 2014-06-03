from django import template
from django.contrib.auth.forms import AuthenticationForm

register = template.Library()

@register.assignment_tag(takes_context=True)
def prepare_login_form(context):
    request = context["request"]
    return AuthenticationForm(request.POST)
