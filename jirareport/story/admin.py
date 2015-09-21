from django.contrib import admin
from story.models import Epic, Story, Status, StoryHistory, Label

# Register your models here.
admin.site.register(Epic)
admin.site.register(Story)
admin.site.register(Status)
admin.site.register(StoryHistory)
admin.site.register(Label)
