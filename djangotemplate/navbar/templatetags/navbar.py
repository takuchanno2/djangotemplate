from django import template
from navbar import navitem_top, NavListItem
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
import copy
from bootstrap3.templatetags import bootstrap3

import time

register = template.Library()

@register.assignment_tag(takes_context=True)
def prepare_navbar(context):
    return list(navitem_top.get_iter(context["request"].path))

@register.filter
def stylize(item, autoescape=None):
    if item.icon:
        icon = bootstrap3.bootstrap_icon(conditional_escape(item.icon))
    else:
        icon = ""

    if item.url:
        output = '<a href="{url}">{icon}{text}</a>'.format(icon=icon, text=conditional_escape(item.title), url=conditional_escape(item.url))
    else:
        output = icon + item.title

    return mark_safe(output)

@register.filter
def make_link(text, url, autoescape=None):
    if url:
        return mark_safe('<a href="{url}">{text}</a>'.format(text=conditional_escape(text), url=conditional_escape(url)))
    else:
        return text

@register.filter
def wrap(text, tag, autoescape=None):
    if url:
        return mark_safe('<{tag}>{text}</{tag}>'.format(text=conditional_escape(text), tag=conditional_escape(text)))
    else:
        return text

stylize.needs_autoescape = True
make_link.needs_autoescape = True
wrap.needs_autospace = True
