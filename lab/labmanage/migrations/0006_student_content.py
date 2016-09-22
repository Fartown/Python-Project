# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0005_auto_20160903_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='content',
            field=models.TextField(verbose_name='内容', null=True, blank=True),
        ),
    ]
