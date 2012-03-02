from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'views.home', name="home"),
	url(r'^hold', 'views.hold', name="hold"),
	url(r'^confirm/(?P<hash>\w+)/$', 'views.confirm'),
)

urlpatterns += staticfiles_urlpatterns()