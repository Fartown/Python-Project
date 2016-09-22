# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0004_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funds',
            name='content',
            field=models.TextField(max_length=300, verbose_name='基金内容'),
        ),
        migrations.AlterField(
            model_name='patent',
            name='content',
            field=models.TextField(max_length=300, verbose_name='专利内容'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile',
            field=models.TextField(null=True, verbose_name='简介', blank=True),
        ),
    ]
