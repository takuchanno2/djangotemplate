#coding:utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from navbar import navitem

navitems =  navitem("アカウント", None, 
                navitem("ログイン", reverse_lazy("accounts:login"), icon="log-in"),
                navitem("ログアウト", reverse_lazy("accounts:logout"), icon="log-out"),
                icon="user"
            )

