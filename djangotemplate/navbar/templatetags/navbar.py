from django import template

register = template.Library()

@register.assignment_tag(takes_context=True)
def empty_tag(context):
    return ""
