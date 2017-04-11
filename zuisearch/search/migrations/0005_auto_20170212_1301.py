# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_home_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='priority',
            field=models.IntegerField(default=0, blank=True, null=True, verbose_name='优先级'),
        ),
        migrations.AlterField(
            model_name='site',
            name='priority',
            field=models.IntegerField(default=0, blank=True, null=True, verbose_name='优先级'),
        ),
    ]
