# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0014_auto_20170113_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='introduce',
            field=models.TextField(null=True, verbose_name='介绍', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='device',
            name='title',
            field=models.CharField(null=True, verbose_name='名称', blank=True, max_length=20),
        ),
    ]
