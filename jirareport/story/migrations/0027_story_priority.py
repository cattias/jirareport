# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0026_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='priority',
            field=models.ForeignKey(related_name='story_priority_set', default=1, to='story.Priority'),
            preserve_default=False,
        ),
    ]
