# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0003_auto_20160802_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, blank=True, null=True, verbose_name='标题')),
                ('content', models.TextField(blank=True, null=True, verbose_name='领域内容')),
                ('tag', models.CharField(max_length=100, verbose_name='类别')),
            ],
            options={
                'verbose_name': '研究领域',
                'verbose_name_plural': '研究领域',
            },
        ),
    ]
