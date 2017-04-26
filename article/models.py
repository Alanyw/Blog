from django.db import models

'''
文章字段
title Char
content Char
author Char(20)
pub_date Date
tag Char(20)

留言字段
article ForeignKey
mailbox Char
mailboxer Char(20)
contact Char(30)
message_date Date
'''


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=20)
    tag = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField


class Mailbox(models.Model):
    article = models.ForeignKey(Article)
    mailbox = models.TextField(blank=True)
    mailboxer = models.CharField(max_length=20)
    contact = models.CharField(max_length=30)
    message_date = models.DateTimeField
