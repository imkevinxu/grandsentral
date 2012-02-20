from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'grandsentral.views.home', name='home'),
    # url(r'^grandsentral/', include('grandsentral.foo.urls')),

    # Uncomment the lines below to enable admin:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'views.home', name="root"),
)

urlpatterns += staticfiles_urlpatterns()