#coding:utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from navbar import item, include, submenu

admin.autodiscover()

navitems = nav_items(
    item("ホーム", reverse_lazy("index"), icon="home"), 
    
)
