# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0020_activitysearch_iati_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='iati_identifier',
            field=models.CharField(db_index=True, max_length=150),
        ),
    ]
