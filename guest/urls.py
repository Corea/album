from django.conf.urls import patterns, include, url

from guest.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', list_picture),
	url(r'^add/$', add_picture),
)
