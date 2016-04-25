# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import ArticleBrief, ArticleContent
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Register your models here.
class ArticleContentInline(admin.TabularInline):
    model = ArticleContent
    extra = 1 

class ArticleBriefAdmin(admin.ModelAdmin):
    fieldsets = [
            ('文章信息', 
                    {'fields': ['article_title', 'article_cut',
                            'article_from']}),
            ('时间信息', {'fields': ['pub_date']}), 
    ]
    list_display = ('article_title', 'article_cut',
            'article_from', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['article_title']
    
    inlines = [ArticleContentInline]

admin.site.register(ArticleBrief, ArticleBriefAdmin)
