# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=50)),
                ('class_info', models.TextField()),
                ('teacher', models.CharField(max_length=50)),
                ('teacher_info', models.TextField()),
                ('groups_info', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(verbose_name='学校', null=True, max_length=50, blank=True)),
                ('qq', models.CharField(verbose_name='QQ号码', null=True, max_length=20, blank=True)),
                ('mobile', models.CharField(verbose_name='手机号码', null=True, max_length=11, unique=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '普通用户',
                'verbose_name_plural': '普通用户',
            },
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('suggestion', models.TextField()),
            ],
            options={
                'verbose_name': '建议',
                'verbose_name_plural': '建议',
            },
        ),
    ]
