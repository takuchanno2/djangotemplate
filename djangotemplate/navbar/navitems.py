#coding:utf-8

from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from navbar import navitem, include
from core import settings

navitems = navitem("navbar", reverse_lazy("navbar:index"), icon="tree-conifer")

