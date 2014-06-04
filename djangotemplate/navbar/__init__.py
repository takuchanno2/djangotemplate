#coding:utf-8

from django.conf import settings
from importlib import import_module
from collections import namedtuple

NavItem = namedtuple("NavItem", "title url icon subitems")
navitem_list = []

def add_navitem_recursively(navitem, list, depth=0):
    list.append({
        "depth": depth,
        "title": navitem.title,
        "url": navitem.url,
        "icon": navitem.icon,
    })

    depth = depth + 1

    for subitem in navitem.subitems:
        add_navitem_recursively(subitem, list, depth)

    return
        
def construct_navbar_structure():
    try:
        navitem_top = import_module(settings.ROOT_NAVBAR_CONF).navitems
    except:
        raise

    add_navitem_recursively(navitem_top, navitem_list)

    return

# titleとmoduleは省略したら、省略先のtopを使うように
def include(module, title=None, url=None, **kwargs):
    mod = import_module(conf)

    navitems = mod.navitems
    navitems.title = title or navitems.title
    navitems.url = url or navitems.url
    navitems.icon = kwargs.get("icon") or navitems.icon

    return navitems

def navitem(title, url, *args, **kwargs):
    return NavItem(title, url, kwargs.get("icon"), args)
