# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0004_activity_normalized_iati_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysector',
            name='sector',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.Sector'),
            preserve_default=False,
        ),
    ]
