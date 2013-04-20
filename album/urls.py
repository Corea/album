from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import os 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'album.views.home', name='home'),
	url(r'^upload/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': os.path.join(os.path.dirname(__file__), '../upload/')}),

    url(r'^guest/', include('guest.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
