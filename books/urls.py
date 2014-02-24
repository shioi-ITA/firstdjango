# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from books.views import *

urlpatterns = patterns('',
    url(r'^$', index),
)

urlpatterns += patterns('',
    # existing patterns here...
    (r'^login/$', login, {'template_name':'books/login.html'}),
)

urlpatterns += patterns('',
    url(r'^author/$', AuthorList.as_view(), name='author-list'),
    url(r'^author/page(?P<page>[0-9]+)/$', AuthorList.as_view(), name='author-list'),
    url(r'^author/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author-detail'),
    url(r'^author/new/$', AuthorCreate.as_view(), name='author-new'),
    url(r'^author/(?P<pk>\d+)/update/$', AuthorUpdate.as_view(), name='author-update'),
    url(r'^author/(?P<pk>\d+)/delete/$', AuthorDelete.as_view(), name='author-delete'),
)

urlpatterns += patterns('',
    url(r'^publisher/$', PublisherList.as_view(), name='publisher-list'),
    url(r'^publisher/page(?P<page>[0-9]+)/$', PublisherList.as_view(), name='publisher-list'),
    url(r'^publisher/(?P<pk>\d+)/$', PublisherDetail.as_view(), name='publisher-detail'),
    url(r'^publisher/new/$', PublisherCreate.as_view(), name='publisher-new'),
    url(r'^publisher/(?P<pk>\d+)/update/$', PublisherUpdate.as_view(), name='publisher-update'),
    url(r'^publisher/(?P<pk>\d+)/delete/$', PublisherDelete.as_view(), name='publisher-delete'),
)

urlpatterns += patterns('',
    url(r'^book/$', BookList.as_view(), name='book-list'),
    url(r'^book/page(?P<page>[0-9]+)/$', BookList.as_view(), name='book-list'),
    url(r'^book/(?P<pk>\d+)/$', BookDetail.as_view(), name='book-detail'),
    url(r'^book/new/$', BookCreate.as_view(), name='book-new'),
    url(r'^book/(?P<pk>\d+)/update/$', BookUpdate.as_view(), name='book-update'),
    url(r'^book/(?P<pk>\d+)/delete/$', BookDelete.as_view(), name='book-delete'),
)
