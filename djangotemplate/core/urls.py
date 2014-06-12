from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
import navbar
from core import settings

admin.autodiscover()
navbar.construct_navbar_structure()

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'djangotemplate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^navbar/', include('navbar.urls', namespace='navbar')),
    url(r'^$', include('main.urls')),
    url(r'^', include('main.urls')),
)
