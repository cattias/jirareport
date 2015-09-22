# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from datetime import datetime

def import_history(apps, schema_editor):
    Story = apps.get_model("story", "Story")
    StoryHistory = apps.get_model("story", "StoryHistory")
    Status = apps.get_model("story", "Status")
    date = datetime.strptime("2015-08-20", "%Y-%m-%d")

    if Story.objects.filter(key='SRMF-164'): StoryHistory(story=Story.objects.filter(key='SRMF-164')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-163'): StoryHistory(story=Story.objects.filter(key='SRMF-163')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-162'): StoryHistory(story=Story.objects.filter(key='SRMF-162')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-161'): StoryHistory(story=Story.objects.filter(key='SRMF-161')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-160'): StoryHistory(story=Story.objects.filter(key='SRMF-160')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-159'): StoryHistory(story=Story.objects.filter(key='SRMF-159')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-158'): StoryHistory(story=Story.objects.filter(key='SRMF-158')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-157'): StoryHistory(story=Story.objects.filter(key='SRMF-157')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-156'): StoryHistory(story=Story.objects.filter(key='SRMF-156')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-155'): StoryHistory(story=Story.objects.filter(key='SRMF-155')[0],status=Status.objects.get(key='Open'),date=date).save()
    
    
    
    
    
    
    if Story.objects.filter(key='SRMF-147'): StoryHistory(story=Story.objects.filter(key='SRMF-147')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-146'): StoryHistory(story=Story.objects.filter(key='SRMF-146')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-145'): StoryHistory(story=Story.objects.filter(key='SRMF-145')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-144'): StoryHistory(story=Story.objects.filter(key='SRMF-144')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-143'): StoryHistory(story=Story.objects.filter(key='SRMF-143')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-142'): StoryHistory(story=Story.objects.filter(key='SRMF-142')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-141'): StoryHistory(story=Story.objects.filter(key='SRMF-141')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-140'): StoryHistory(story=Story.objects.filter(key='SRMF-140')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-139'): StoryHistory(story=Story.objects.filter(key='SRMF-139')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-138'): StoryHistory(story=Story.objects.filter(key='SRMF-138')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-133'): StoryHistory(story=Story.objects.filter(key='SRMF-133')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-123'): StoryHistory(story=Story.objects.filter(key='SRMF-123')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-122'): StoryHistory(story=Story.objects.filter(key='SRMF-122')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-121'): StoryHistory(story=Story.objects.filter(key='SRMF-121')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-120'): StoryHistory(story=Story.objects.filter(key='SRMF-120')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-117'): StoryHistory(story=Story.objects.filter(key='SRMF-117')[0],status=Status.objects.get(key='In Progress'),date=date).save()
    if Story.objects.filter(key='SRMF-116'): StoryHistory(story=Story.objects.filter(key='SRMF-116')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-115'): StoryHistory(story=Story.objects.filter(key='SRMF-115')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-114'): StoryHistory(story=Story.objects.filter(key='SRMF-114')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-113'): StoryHistory(story=Story.objects.filter(key='SRMF-113')[0],status=Status.objects.get(key='In Progress'),date=date).save()
    if Story.objects.filter(key='SRMF-112'): StoryHistory(story=Story.objects.filter(key='SRMF-112')[0],status=Status.objects.get(key='In Progress'),date=date).save()
    if Story.objects.filter(key='SRMF-111'): StoryHistory(story=Story.objects.filter(key='SRMF-111')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-110'): StoryHistory(story=Story.objects.filter(key='SRMF-110')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-109'): StoryHistory(story=Story.objects.filter(key='SRMF-109')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-108'): StoryHistory(story=Story.objects.filter(key='SRMF-108')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-107'): StoryHistory(story=Story.objects.filter(key='SRMF-107')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-106'): StoryHistory(story=Story.objects.filter(key='SRMF-106')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-105'): StoryHistory(story=Story.objects.filter(key='SRMF-105')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-104'): StoryHistory(story=Story.objects.filter(key='SRMF-104')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-103'): StoryHistory(story=Story.objects.filter(key='SRMF-103')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-102'): StoryHistory(story=Story.objects.filter(key='SRMF-102')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-101'): StoryHistory(story=Story.objects.filter(key='SRMF-101')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-100'): StoryHistory(story=Story.objects.filter(key='SRMF-100')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-99'): StoryHistory(story=Story.objects.filter(key='SRMF-99')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-98'): StoryHistory(story=Story.objects.filter(key='SRMF-98')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-97'): StoryHistory(story=Story.objects.filter(key='SRMF-97')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-96'): StoryHistory(story=Story.objects.filter(key='SRMF-96')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-95'): StoryHistory(story=Story.objects.filter(key='SRMF-95')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-94'): StoryHistory(story=Story.objects.filter(key='SRMF-94')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-93'): StoryHistory(story=Story.objects.filter(key='SRMF-93')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-92'): StoryHistory(story=Story.objects.filter(key='SRMF-92')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-91'): StoryHistory(story=Story.objects.filter(key='SRMF-91')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-90'): StoryHistory(story=Story.objects.filter(key='SRMF-90')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-89'): StoryHistory(story=Story.objects.filter(key='SRMF-89')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-81'): StoryHistory(story=Story.objects.filter(key='SRMF-81')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-80'): StoryHistory(story=Story.objects.filter(key='SRMF-80')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-79'): StoryHistory(story=Story.objects.filter(key='SRMF-79')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-78'): StoryHistory(story=Story.objects.filter(key='SRMF-78')[0],status=Status.objects.get(key='In Progress'),date=date).save()
    if Story.objects.filter(key='SRMF-71'): StoryHistory(story=Story.objects.filter(key='SRMF-71')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-70'): StoryHistory(story=Story.objects.filter(key='SRMF-70')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-69'): StoryHistory(story=Story.objects.filter(key='SRMF-69')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-68'): StoryHistory(story=Story.objects.filter(key='SRMF-68')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-67'): StoryHistory(story=Story.objects.filter(key='SRMF-67')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-66'): StoryHistory(story=Story.objects.filter(key='SRMF-66')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-65'): StoryHistory(story=Story.objects.filter(key='SRMF-65')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-64'): StoryHistory(story=Story.objects.filter(key='SRMF-64')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-63'): StoryHistory(story=Story.objects.filter(key='SRMF-63')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-62'): StoryHistory(story=Story.objects.filter(key='SRMF-62')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-61'): StoryHistory(story=Story.objects.filter(key='SRMF-61')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-60'): StoryHistory(story=Story.objects.filter(key='SRMF-60')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-59'): StoryHistory(story=Story.objects.filter(key='SRMF-59')[0],status=Status.objects.get(key='Resolved'),date=date).save()
    if Story.objects.filter(key='SRMF-54'): StoryHistory(story=Story.objects.filter(key='SRMF-54')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-53'): StoryHistory(story=Story.objects.filter(key='SRMF-53')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-51'): StoryHistory(story=Story.objects.filter(key='SRMF-51')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-50'): StoryHistory(story=Story.objects.filter(key='SRMF-50')[0],status=Status.objects.get(key='Resolved'),date=date).save()
    if Story.objects.filter(key='SRMF-32'): StoryHistory(story=Story.objects.filter(key='SRMF-32')[0],status=Status.objects.get(key='In Progress'),date=date).save()
    if Story.objects.filter(key='SRMF-31'): StoryHistory(story=Story.objects.filter(key='SRMF-31')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-30'): StoryHistory(story=Story.objects.filter(key='SRMF-30')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-29'): StoryHistory(story=Story.objects.filter(key='SRMF-29')[0],status=Status.objects.get(key='In Progress'),date=date).save()
    if Story.objects.filter(key='SRMF-27'): StoryHistory(story=Story.objects.filter(key='SRMF-27')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-26'): StoryHistory(story=Story.objects.filter(key='SRMF-26')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-25'): StoryHistory(story=Story.objects.filter(key='SRMF-25')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-22'): StoryHistory(story=Story.objects.filter(key='SRMF-22')[0],status=Status.objects.get(key='In Progress'),date=date).save()
    if Story.objects.filter(key='SRMF-5'): StoryHistory(story=Story.objects.filter(key='SRMF-5')[0],status=Status.objects.get(key='Open'),date=date).save()
    if Story.objects.filter(key='SRMF-4'): StoryHistory(story=Story.objects.filter(key='SRMF-4')[0],status=Status.objects.get(key='In Progress'),date=date).save()


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_auto_20150921_2316'),
    ]

    operations = [
                  migrations.RunPython(import_history),
    ]
