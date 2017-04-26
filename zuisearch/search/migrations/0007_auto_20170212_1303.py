# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20170212_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='introduce',
            field=models.TextField(max_length=200, blank=True, verbose_name='介绍', null=True),
        ),
    ]
