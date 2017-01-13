# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0013_auto_20170113_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='introduce',
            field=models.TextField(verbose_name='介绍', null=True, max_length=400, blank=True),
        ),
    ]
