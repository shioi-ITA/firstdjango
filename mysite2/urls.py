# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^books/', include('books.urls', namespace="books")),
    (r'^login/$', login, {'template_name':'registration/login.html'}),
    (r'^logout/$', logout, {'template_name':'registration/logout.html'}),
)

urlpatterns += patterns('',
    # existing patterns here...
    (r'^search/$', 'search.views.search'),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': 'C:/python_study/tinymce_4.0.20/tinymce/js/tinymce/' }),
    #(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': 'C:/python_study/tinymce_3.5.10/tinymce/jscripts/tiny_mce/' }),
    (r'', include('django.contrib.flatpages.urls')),
)
