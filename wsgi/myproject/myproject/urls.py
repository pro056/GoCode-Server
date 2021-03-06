from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
import requests

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^createuser/$', createUser),
    url(r'^test/$', index),
    url(r'^sethandle/$', setHandle),
    url(r'^getusers/$', getUsers),
    url(r'^update/$', update),
    url(r'^getpastcontest/$', getPastContests),
    url(r'^getcurrentcontest/$', getCurrContests),
    url(r'^getfuturecontest/$', getFutureContests),
    url(r'^getall/$', getAllContests)
)
