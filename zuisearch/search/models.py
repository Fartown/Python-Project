# coding:utf-8
from django.db import models

# Create your models here.
class Column(models.Model):
    name = models.CharField(u'分类名称', max_length=12, blank=True, null=True)
    class Meta:
        verbose_name = u'分类管理'
        verbose_name_plural = u'分类管理'
    def __str__(self):
        return self.name
class Site(models.Model):
    column = models.ForeignKey(Column, blank=True, null=True, verbose_name='栏目分类')
    title = models.CharField(u'名称', max_length=12, blank=True, null=True)
    introduce = models.TextField(u'组织介绍', max_length=200, blank=True, null=True)
    siteurl = models.CharField(u'网站地址', max_length=100, blank=True, null=True)
    wxname = models.CharField(u'官方微信名', max_length=30, blank=True, null=True)
    wxintro = models.CharField(u'微信简介', max_length=100, blank=True, null=True)
    wxid = models.CharField(u'微信ID', max_length=30, blank=True, null=True)
    wxcode = models.ImageField(upload_to='qrimg', blank=True, null=True, verbose_name='微信二维码')
    wbname = models.CharField(u'官方微博名', max_length=30, blank=True, null=True)
    wburl = models.CharField(u'微博地址', max_length=30, blank=True, null=True)
    priority = models.IntegerField(u'优先级', blank=True, null=True, default=0)
    activate = models.BooleanField(u'审核通过', blank=True, default=True)
    class Meta:
        verbose_name = u'网站管理'
        verbose_name_plural = u'网站管理'
    def __str__(self):
        return self.title
class Home(models.Model):
    title = models.CharField(u'名称', max_length=12, blank=True, null=True)
    siteurl = models.CharField(u'网站地址', max_length=100, blank=True, null=True)
    priority = models.IntegerField(u'优先级', blank=True, null=True, default=0)
    position = models.BooleanField(u'校内网站', blank=True)
    class Meta:
        verbose_name = u'首页站点'
        verbose_name_plural = u'首页站点'
    def __str__(self):
        return str(self.title)