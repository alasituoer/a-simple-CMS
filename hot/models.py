# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
from django.utils import timezone

# Create your models here.
class ArticleBrief(models.Model):
    article_title = models.CharField('标题', max_length=200)
    article_cut = models.TextField('简介', max_length=1000)
    article_from = models.CharField('来源', max_length=50)
    pub_date = models.DateTimeField('发布时间')

    def __str__(self):
        return self.article_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class ArticleContent(models.Model):
    articlebrief = models.ForeignKey(ArticleBrief)
    article_text = UEditorField('文章', height=300, width=1000, 
            default=u'', blank=True, imagePath='uploads/images/',
            filePath='uploads/files/', toolbars='full',)

