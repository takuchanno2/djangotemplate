from django.conf.urls import patterns, include, url
from django.contrib import admin
from navbar.views import NavbarExampleView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', NavbarExampleView.as_view(), name='example'),
    url(r'^(?P<pk>.*)/$', NavbarExampleView.as_view()),
)
