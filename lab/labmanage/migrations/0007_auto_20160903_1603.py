# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0006_student_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile',
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(upload_to='photos', default=datetime.datetime(2016, 9, 3, 8, 3, 57, 75014, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='简介'),
        ),
    ]
