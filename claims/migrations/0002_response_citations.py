# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-22 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='citations',
            field=models.ManyToManyField(related_name='cited_by', to='claims.Claim'),
        ),
    ]
