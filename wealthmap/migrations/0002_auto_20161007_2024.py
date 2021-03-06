# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-07 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wealthmap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='agency',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wealthmap.AgencyProvider'),
        ),
    ]
