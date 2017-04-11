# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20170212_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name_plural': '首页站点', 'verbose_name': '首页站点'},
        ),
        migrations.AddField(
            model_name='site',
            name='wburl',
            field=models.CharField(null=True, verbose_name='微博地址', blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='site',
            name='wbname',
            field=models.CharField(null=True, verbose_name='官方微博名', blank=True, max_length=20),
        ),
    ]
