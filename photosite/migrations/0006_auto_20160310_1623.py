# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photosite', '0005_auto_20160310_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_title',
            field=models.CharField(help_text=b'The name of the category.', max_length=20),
        ),
    ]