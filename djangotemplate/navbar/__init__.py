#coding:utf-8

from django.conf import settings
from importlib import import_module
from collections import namedtuple
from django.utils.encoding import python_2_unicode_compatible

# リスト形式に変換されたメニュー項目(NavListItem)一覧
navitem_list = []

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

    def to_list_item(self):
        return NavListItem(0, self.title, self.url, self.icon)

    @staticmethod
    def _add_to_list(list, item, depth=0):
        list_item = item.to_list_item()
        list_item.depth = depth
        list_item.attribute = ("begin-sub" if item.subitems else None)
        list.append(list_item)

        depth = depth + 1

        for subitem in item.subitems:
            NavItem._add_to_list(list, subitem, depth)

        if item.subitems:
            list.append(NavListItem(depth, attribute="end-sub"))

    def to_list2(self):
        """
        NavListItemのリスト形式に変換
        """
        list = []
        NavItem._add_to_list(list, self)

        if self.subitems:
            list.append(NavListItem(0, attribute="end-sub"))

        return list

    def to_list(self):
        """
        深さ優先でトラバース
        """

        stack = [(0, self)]

        while stack:
            (depth, item) = stack.pop()
            print((">" * depth) + " " + item.title)

            depth = depth + 1
            for sub in reversed(item.subitems):
                stack.append((depth, sub))

        return self.to_list2()
    
    @python_2_unicode_compatible
    def __str__(self):
        return str(self.__dict__)
        
def construct_navbar_structure():
    try:
        navitem_top = import_module(settings.ROOT_NAVBAR_CONF).navitems
    except:
        raise

    global navitem_list
    navitem_list = navitem_top.to_list()

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
