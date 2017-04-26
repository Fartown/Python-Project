# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20170212_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='wxintro',
            field=models.CharField(blank=True, null=True, max_length=100, verbose_name='微信简介'),
        ),
    ]
