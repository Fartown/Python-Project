# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20170212_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='introduce',
            field=models.TextField(null=True, blank=True, verbose_name='组织介绍', max_length=200),
        ),
    ]
