# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20170212_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='wxcode',
            field=models.ImageField(verbose_name='微信二维码', blank=True, upload_to='qrimg', null=True),
        ),
    ]
