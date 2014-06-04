from django import template
from navbar import navitem_list

register = template.Library()

@register.assignment_tag(takes_context=True)
def prepare_navbar(context):
    return navitem_list
