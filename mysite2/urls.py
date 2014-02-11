# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('books.urls', namespace="books")),
)

urlpatterns += patterns('',
    # existing patterns here...
    (r'^login/$', login, { 'template_name':'login.html'}),
    (r'^logout/$', logout, {'template_name':'logout.html'}),
)
