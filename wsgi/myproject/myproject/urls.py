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
    url(r'^test/$', index)
    
)
