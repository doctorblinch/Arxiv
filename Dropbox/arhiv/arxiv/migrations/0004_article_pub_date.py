# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161020145901 on 2016-12-09 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arxiv', '0003_article_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=1, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
