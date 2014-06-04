from django.conf.urls import patterns, include, url
from django.contrib import admin
from navbar.views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
)
