#coding:utf-8

from django.conf import settings
from importlib import import_module
from collections import namedtuple

NavItem = namedtuple("NavItem", "title icon url")
NavItemGroup = namedtuple("NavItemGroup", "title icon items")

def construct_navbar_structure():
    try:
        conf = settings.ROOT_NAVBAR_CONF
    except:
        raise

    mod = import_module(conf)
    pass

# メニューのrootの要素のtitle, iconはbrandとして表示するか
def item_group(title, *args, icon=None):
    return NavItemGroup(title, icon, args)

# titleとmoduleは省略したら、省略先のtopを使うように
def include(module, title=None, icon=None):
    mod = import_module(conf)

    navitems = mod.navitems
    navitems.title = title or navitems.title
    navitems.icon = icon or navitems.icon

    return navitems

def item(title, url, icon=None):
    return NavItem(title, icon, url)
