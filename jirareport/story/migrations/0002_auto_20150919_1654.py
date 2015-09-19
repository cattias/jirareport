# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epic',
            name='tags',
            field=models.ManyToManyField(related_name='epic_label_set', to='story.Label', blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(related_name='story_label_set', to='story.Label', blank=True),
        ),
    ]
