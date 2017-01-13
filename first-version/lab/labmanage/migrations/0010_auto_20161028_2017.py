# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0009_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('content', models.TextField(verbose_name='关于我们', blank=True, null=True)),
            ],
            options={
                'verbose_name': '关于我们',
                'verbose_name_plural': '关于我们',
            },
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '首页轮播图', 'verbose_name_plural': '首页轮播图'},
        ),
    ]
