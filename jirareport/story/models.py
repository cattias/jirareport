from django.db import models

# Create your models here.
class Label(models.Model):
    key = models.CharField(max_length=255, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)

class Status(models.Model):
    key = models.CharField(max_length=255, unique=True)
    title = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

class Epic(models.Model):
    key = models.CharField(max_length=255, unique=True)
    title = models.TextField()
    tags = models.ManyToManyField(Label, related_name='epic_label_set', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

class Story(models.Model):
    key = models.CharField(max_length=255, unique=True)
    title = models.TextField()
    tags = models.ManyToManyField(Label, related_name='story_label_set', blank=True)
    epic = models.ForeignKey(Epic, related_name='story_epic_set')
    creation_date = models.DateTimeField(auto_now_add=True)

class StoryHistory(models.Model):
    story = models.ForeignKey(Story, related_name='story_history_set')
    status = models.ForeignKey(Status, related_name='status_history_set')
    date = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)
