# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('title', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('title', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('title', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('epic', models.ForeignKey(related_name='story_epic_set', to='story.Epic')),
                ('tags', models.ManyToManyField(related_name='story_label_set', null=True, to='story.Label', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoryHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.ForeignKey(related_name='status_history_set', to='story.Status')),
                ('story', models.ForeignKey(related_name='story_history_set', to='story.Story')),
            ],
        ),
        migrations.AddField(
            model_name='epic',
            name='tags',
            field=models.ManyToManyField(related_name='epic_label_set', null=True, to='story.Label', blank=True),
        ),
    ]
