#coding:utf-8

from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from navbar import item_group, item, include
from core import settings

navitems = item_group(settings.PROJECT_NAME, 
    item("ホーム", reverse_lazy("index"), icon="home"), 
    item_group("検索エンジン", 
        item("Google", "http://google.com/"),
        item("Yahoo", "http://yahoo.co.jp/"),
        item("Bing", "http://bing.jp/"),
    ),
    # include() # ←acountsあたりを読む
)

print("hoge")
