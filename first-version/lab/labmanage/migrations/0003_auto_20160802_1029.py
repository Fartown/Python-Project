# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0002_auto_20160801_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='img',
        ),
        migrations.AlterField(
            model_name='student',
            name='profile',
            field=models.TextField(verbose_name='简介'),
        ),
    ]
