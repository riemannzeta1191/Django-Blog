# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-26 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170226_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postDetail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.PostDetail'),
        ),
    ]
