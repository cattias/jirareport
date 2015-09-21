# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20150919_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epic',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
