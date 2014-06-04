from django import template
from navbar import navitem_list
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

register = template.Library()

@register.assignment_tag(takes_context=True)
def prepare_navbar(context):
    return navitem_list

@register.filter
def make_link(text, url, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    if url:
        return mark_safe('<a href="{0}">{1}</a>'.format(esc(url), esc(text)))
    else:
        return text

make_link.needs_autoescape = True