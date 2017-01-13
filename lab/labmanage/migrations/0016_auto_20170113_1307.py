# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0015_auto_20170113_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='introduce',
            field=models.TextField(verbose_name='介绍', blank=True, max_length=80, null=True),
        ),
    ]
