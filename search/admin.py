# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from search.models import SearchKeyword

class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword

class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)
