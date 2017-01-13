# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0011_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='title',
            field=models.CharField(null=True, blank=True, max_length=400, verbose_name='介绍'),
        ),
    ]
