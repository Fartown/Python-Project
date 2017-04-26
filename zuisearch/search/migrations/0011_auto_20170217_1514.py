# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_auto_20170213_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='activate',
            field=models.BooleanField(default=True, verbose_name='校内网站'),
        ),
        migrations.AlterField(
            model_name='home',
            name='siteurl',
            field=models.CharField(verbose_name='网站地址', blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='siteurl',
            field=models.CharField(verbose_name='网站地址', blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='wbname',
            field=models.CharField(verbose_name='官方微博名', blank=True, max_length=30, null=True),
        ),
    ]
