from django.conf.urls import patterns, include, url
from django.contrib import admin
import navbar

admin.autodiscover()
navbar.construct_navbar_structure()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotemplate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^$', include('main.urls')),
    url(r'^', include('main.urls')),
)
