# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0010_auto_20161028_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(blank=True, null=True, verbose_name='名称', max_length=100)),
                ('img', models.ImageField(verbose_name='仪器设备', upload_to='device')),
            ],
            options={
                'verbose_name_plural': '仪器设备',
                'verbose_name': '仪器设备',
            },
        ),
    ]
