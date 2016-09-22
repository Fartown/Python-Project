# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='content',
            field=models.TextField(null=True, blank=True, verbose_name='工程应用内容'),
        ),
    ]
