# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='分类名称', blank=True, null=True, max_length=12)),
            ],
            options={
                'verbose_name_plural': '分类管理',
                'verbose_name': '分类管理',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='名称', blank=True, null=True, max_length=12)),
                ('siteurl', models.CharField(verbose_name='网站地址', blank=True, null=True, max_length=30)),
                ('position', models.BooleanField(verbose_name='校内网站')),
            ],
            options={
                'verbose_name_plural': '网站管理',
                'verbose_name': '首页站点',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='名称', blank=True, null=True, max_length=12)),
                ('introduce', models.CharField(verbose_name='介绍', blank=True, null=True, max_length=200)),
                ('siteurl', models.CharField(verbose_name='网站地址', blank=True, null=True, max_length=30)),
                ('wxname', models.CharField(verbose_name='官方微信名', blank=True, null=True, max_length=30)),
                ('wxid', models.CharField(verbose_name='微信ID', blank=True, null=True, max_length=30)),
                ('wxcode', models.ImageField(upload_to='qrimg', blank=True, null=True)),
                ('wbname', models.CharField(verbose_name='微博地址', blank=True, null=True, max_length=30)),
                ('priority', models.IntegerField(verbose_name='优先级', blank=True, null=True, max_length=30)),
                ('cloumn', models.ForeignKey(blank=True, verbose_name='栏目分类', null=True, to='search.Column')),
            ],
            options={
                'verbose_name_plural': '网站管理',
                'verbose_name': '网站管理',
            },
        ),
    ]
