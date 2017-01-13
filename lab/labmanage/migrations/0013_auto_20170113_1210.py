# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0012_auto_20170113_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='introduce',
            field=models.CharField(null=True, max_length=400, verbose_name='介绍', blank=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='title',
            field=models.CharField(null=True, max_length=100, verbose_name='名称', blank=True),
        ),
    ]
