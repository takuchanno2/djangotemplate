from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import * 

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotemplate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TopPageView.as_view(), name="top"),
    url(r'^(?P<pk>.*)/$', TopPageView.as_view(), name="top"),
)
