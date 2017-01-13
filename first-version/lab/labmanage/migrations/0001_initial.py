# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateTimeField(verbose_name='标题', auto_now=True)),
                ('title', models.CharField(verbose_name='标题', blank=True, max_length=100, null=True)),
                ('content', models.CharField(verbose_name='工程应用内容', max_length=300)),
            ],
            options={
                'verbose_name': '工程应用',
                'verbose_name_plural': '工程应用',
            },
        ),
        migrations.CreateModel(
            name='Funds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(verbose_name='基金内容', max_length=300)),
            ],
            options={
                'verbose_name': '基金',
                'verbose_name_plural': '基金',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='标题', blank=True, max_length=100, null=True)),
                ('img', models.CharField(verbose_name='插图', blank=True, max_length=500, null=True)),
                ('content', models.TextField(verbose_name='内容', blank=True, null=True)),
                ('views', models.IntegerField(verbose_name='点击次数', default=0)),
                ('add_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '新闻',
                'ordering': ['-add_date'],
                'verbose_name_plural': '新闻',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(verbose_name='论文', max_length=300)),
                ('year', models.IntegerField(verbose_name='年份')),
            ],
            options={
                'verbose_name': '论文',
                'verbose_name_plural': '论文',
            },
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(verbose_name='专利内容', max_length=300)),
            ],
            options={
                'verbose_name': '专利',
                'verbose_name_plural': '专利',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='名字', blank=True, max_length=100, null=True)),
                ('education', models.CharField(verbose_name='学历', max_length=100)),
                ('profile', models.CharField(verbose_name='简介', max_length=300)),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
    ]
