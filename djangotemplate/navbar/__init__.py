#coding:utf-8

from django.conf import settings
from importlib import import_module
from collections import namedtuple

NavItem = namedtuple("NavItem", "title url icon subitems")
navitem_list = []

NavListItem = namedtuple("NavListItem", "depth attribute title url icon active")

def add_navitem_recursively(navitem, list, depth=0):
    list.append(NavListItem(
        depth,
        ("begin-sub" if navitem.subitems else None),
        navitem.title, navitem.url, navitem.icon, False
    ))

    depth = depth + 1

    for subitem in navitem.subitems:
        add_navitem_recursively(subitem, list, depth)

    if navitem.subitems:
        list.append(NavListItem(depth, "end-sub", None, None, None, False))

    return
        
def construct_navbar_structure():
    try:
        navitem_top = import_module(settings.ROOT_NAVBAR_CONF).navitems
    except:
        raise

    add_navitem_recursively(navitem_top, navitem_list)

    if navitem_top.subitems:
        navitem_list.append(NavListItem(0, "end-sub", None, None, None, False))

    return

# titleとmoduleは省略したら、省略先のtopを使うように
def include(module, title=None, url=None, **kwargs):
    navitems = import_module(module).navitems

    return NavItem(
        title or navitems.title,
        url or navitems.url, 
        kwargs.get("icon") or navitems.icon,
        navitems.subitems
    )

def navitem(title, url, *args, **kwargs):
    return NavItem(title, url, kwargs.get("icon"), args)
