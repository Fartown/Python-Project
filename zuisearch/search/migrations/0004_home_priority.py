# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20170212_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='priority',
            field=models.IntegerField(blank=True, verbose_name='优先级', null=True),
        ),
    ]
