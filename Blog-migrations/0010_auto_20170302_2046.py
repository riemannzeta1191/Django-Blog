# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-02 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170301_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postDetail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.PostDetail'),
        ),
    ]
