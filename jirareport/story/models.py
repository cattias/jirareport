from django.db import models

# Create your models here.
class Label(models.Model):
    key = models.CharField(max_length=255, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.key

class Status(models.Model):
    key = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key

class Epic(models.Model):
    key = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Label, related_name='epic_label_set', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key + " - " + self.title

class Story(models.Model):
    key = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Label, related_name='story_label_set', blank=True)
    epic = models.ForeignKey(Epic, related_name='story_epic_set')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key + " - " + self.title

class StoryHistory(models.Model):
    story = models.ForeignKey(Story, related_name='story_history_set')
    status = models.ForeignKey(Status, related_name='status_history_set')
    date = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.story + " - " + self.status
