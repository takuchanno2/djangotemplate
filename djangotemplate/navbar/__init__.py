#coding:utf-8

from django.conf import settings
from importlib import import_module
from collections import namedtuple
from django.utils.encoding import python_2_unicode_compatible

import time

# NavBarの先頭要素
navitem_top = None

class NavListItem:
    """
    メニューの1つ1つの項目を表現するクラス
    depthが項目が配置された階層を表現し、メニュー構造をリスト+階層情報で表現する
    子項目を持つ項目(親項目)のattributeには"begin-sub"が設定される
    また、attributeが"end-sub"な要素は、子項目の終了位置を示す
    """
    def __init__(self, depth, title=None, url=None, icon=None, attribute=None, active=False):
        self.depth = depth
        self.title = title
        self.url = url
        self.icon = icon
        self.attribute = attribute
        self.active = active

    @python_2_unicode_compatible
    def __str__(self):
        return str(self.__dict__)

class NavItem:
    """
    メニューの1つ1つの項目を表現するクラス
    メニュー構造をツリーで表現する
    """

    def __init__(self, title, url=None, icon=None, subitems=None):
        self.title = title
        self.url = url
        self.icon = icon
        self.subitems = subitems

    def __iter__(self):
        return self.get_iter(self, None)

    def get_iter(self, active_url = None):
        """
        深さ優先でトラバース
        """

        stack = [(0, self)]

        while stack:
            (depth, item) = stack.pop()

            if not item:
                yield NavListItem(depth, attribute="end-sub")   
            else:
                yield NavListItem(depth, item.title, item.url, item.icon, ("begin-sub" if item.subitems else None), (item.url == active_url))

                if item.subitems:
                    stack.append((depth, None))

                    depth = depth + 1
                    for sub in reversed(item.subitems):
                        stack.append((depth, sub))
    
    @python_2_unicode_compatible
    def __str__(self):
        return str(self.__dict__)
        
def construct_navbar_structure():
    try:
        global navitem_top
        navitem_top = import_module(settings.ROOT_NAVBAR_CONF).navitems
    except:
        raise

    return

# titleとmoduleは省略したら、省略先のtopを使うように
def include(module, title=None, url=None, **kwargs):
    navitems = import_module(module).navitems

    navitems.title = title or navitems.title
    navitems.url = url or navitems.url
    navitems.icon = kwargs.get("icon") or navitems.icon

    return navitems

def navitem(title, url, *args, **kwargs):
    return NavItem(title, url, kwargs.get("icon"), args)
