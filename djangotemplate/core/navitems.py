#coding:utf-8

from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from navbar import navitem, include
from core import settings

navitems = navitem(settings.PROJECT_NAME, reverse_lazy("index"),
    navitem("ホーム", reverse_lazy("index"), icon="home"), 
    navitem("検索エンジン", None,
        navitem("Google", "http://google.com/"),
        navitem("Yahoo", "http://yahoo.co.jp/"),
        navitem("Bing", "http://bing.jp/"),
    ),
    # include() # ←acountsあたりを読む
)

