from django import template

register = template.Library()

@register.assignment_tag(takes_context=True)
def prepare_navbar(context):
    return ""
