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

class Priority(models.Model):
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

    @staticmethod
    def CreateEpicFromExcel(key, title, labels):
        epic = None
        if Epic.objects.filter(key=key):
            epic = Epic.objects.get(key=key)
        else:
            epic = Epic(key=key, title=title)
        epic.title = title
        epic.save()
        
        epic.tags.clear()
        tags = labels.split(",")
        for t in tags:
            t = t.strip()
            if t:
                tag = Label.objects.get_or_create(key=t)[0]
                epic.tags.add(tag)

class Story(models.Model):
    key = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Label, related_name='story_label_set', blank=True)
    priority = models.ForeignKey(Priority, related_name='story_priority_set', default=1)
    epic = models.ForeignKey(Epic, related_name='story_epic_set')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key + " - " + self.title
    
    @staticmethod
    def CreateHistoryFromExcel(key, title, labels, priority, epicname, status, date):
        epic = Epic.objects.get(title=epicname)
        prio = Priority.objects.get_or_create(key=priority,title=priority)[0]
        st = Status.objects.get_or_create(key=status,title=status)[0]
        
        if Story.objects.filter(key=key):
            story = Story.objects.get(key=key)
        else:
            story = Story(key=key, title=title, epic=epic, priority=prio)
        story.title = title
        story.epic = epic
        story.priority = prio
        story.save()
        
        story.tags.clear()
        tags = labels.split(",")
        for t in tags:
            t = t.strip()
            if t:
                tag = Label.objects.get_or_create(key=t)[0]
                story.tags.add(tag)
        
        StoryHistory(story=story, status=st, date=date).save()
        
class StoryHistory(models.Model):
    story = models.ForeignKey(Story, related_name='story_history_set')
    status = models.ForeignKey(Status, related_name='status_history_set')
    date = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.story, self.status)
