# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
# Create your models here.
class Engineer(models.Model):
    add_date = models.DateTimeField(auto_now=True, verbose_name='标题')
    title = models.CharField(blank=True, null=True, max_length=100, verbose_name='标题')
    content = models.TextField(blank=True, null=True, verbose_name='工程应用内容')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '工程应用'
        verbose_name_plural = verbose_name


class Funds(models.Model):
    content = models.TextField(max_length=300, verbose_name='基金内容')

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '基金'
        verbose_name_plural = verbose_name


class Paper(models.Model):
    content = models.CharField(max_length=300, verbose_name='论文')
    year = models.IntegerField(verbose_name='年份')

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '论文'
        verbose_name_plural = verbose_name


class Patent(models.Model):
    content = models.TextField(max_length=300, verbose_name='专利内容')

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '专利'
        verbose_name_plural = verbose_name


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='名字')
    education = models.CharField(max_length=100, verbose_name='学历')
    image = models.ImageField(upload_to='photos')
    content = models.TextField(blank=True, null=True, verbose_name='简介')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name


class News(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='标题')
    image = models.ImageField(upload_to='photos', blank=True, null=True, verbose_name='首页封面图')
    content = models.TextField(blank=True, null=True, verbose_name='内容')
    views = models.IntegerField(default=0, verbose_name='点击次数')  # 点击率
    add_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    # def getCount(self):
    #     return News.objects.filter(type=self.id).count()
    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
        ordering = ['-add_date']
class Field(models.Model):
    tag = models.CharField(max_length=100,verbose_name='类别')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='标题')
    content = models.TextField(blank=True, null=True, verbose_name='领域内容')
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '研究领域'
        verbose_name_plural = verbose_name
class Banner(models.Model):
    img = models.ImageField(upload_to='banner',verbose_name='首页轮播图')
    title = '轮播图'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '首页轮播图'
        verbose_name_plural = verbose_name
class Device(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True, verbose_name='名称')
    introduce = models.TextField(max_length=80, blank=True, null=True, verbose_name='介绍')
    img = models.ImageField(upload_to='device',verbose_name='仪器设备')
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '仪器设备'
        verbose_name_plural = verbose_name
    # def __str__(self):
    #     return self.img\
class About(models.Model):
    content = models.TextField(blank=True, null=True, verbose_name='关于我们')
    title = '关于我们的介绍'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '关于我们'
        verbose_name_plural = verbose_name