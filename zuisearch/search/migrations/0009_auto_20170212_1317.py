# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_site_wxintro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='cloumn',
            new_name='column',
        ),
    ]
