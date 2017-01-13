# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('labmanage', '0007_auto_20160903_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='photos', default=datetime.datetime(2016, 9, 5, 1, 37, 59, 905035, tzinfo=utc), verbose_name='首页封面图'),
            preserve_default=False,
        ),
    ]
