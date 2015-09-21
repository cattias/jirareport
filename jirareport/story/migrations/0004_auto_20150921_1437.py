# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def import_epics(apps, schema_editor):
    Epic = apps.get_model("story", "Epic")
    Label = apps.get_model("story", "Label")
    ACS_10 = Label.objects.get(key="ACS_1.0")
    ACS_11 = Label.objects.get(key="ACS_1.1")
    ACS_12 = Label.objects.get(key="ACS_1.2")
    HMP_SRE = Label.objects.get(key="HMP-SRE")
    ACS = Label.objects.get(key="ACS")
    AHP = Label.objects.get(key="AHP")
    admin_services = Label.objects.get(key="admin_services")
    
    e=Epic(key='SRMF-525',title='Capability to configure the framework');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-520',title='Remove buckets - Couchbase');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-519',title='Create new buckets - Couchbase');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-516',title='Remove a DB component - Oracle');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-513',title='Create a new DB component - Oracle');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-445',title='Addition of a new set of machines into a CouchBase cluster');e.save();e.tags.add(ACS_12)
    e=Epic(key='SRMF-444',title='Deletion of an existing set of machines from a CouchBase cluster');e.save();e.tags.add(ACS_12)
    e=Epic(key='SRMF-443',title='Fallback an existing version of CouchBase');e.save();e.tags.add(ACS_12)
    e=Epic(key='SRMF-442',title='Activate a new version of CouchBase');e.save();e.tags.add(ACS_12)
    e=Epic(key='SRMF-441',title='Removing an existing view document from CouchBase');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-440',title='Applying a new view document on CouchBase');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-439',title='Fallback an online data change on Couchbase');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-438',title='Apply an online data change on Couchbase');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-437',title='Falling Back a DDL in Oracle');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-436',title='Applying a DDL on Oracle');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-435',title='Fallback an online data change (DML) on Oracle');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-434',title='Apply an online data change (DML) on Oracle');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-433',title='Oracle Backups');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-430',title='Force the propagation of a `static` fileset');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-429',title='Resume the traffic to a POD');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-428',title='Suspend traffic to a POD');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-427',title='Resume the traffic on a Zone');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-426',title='Isolate an Isolation Zone');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-293',title='Deploy Redundant S-Filer in US Data-Center to Support AHP/HMP');e.save();e.tags.add(HMP_SRE)
    e=Epic(key='SRMF-291',title='Deploy S-Filer in US Data-Center to Support AHP/HMP');e.save();e.tags.add(HMP_SRE)
    e=Epic(key='SRMF-251',title='AHP:Global Integration on ACS');e.save();e.tags.add(AHP)
    e=Epic(key='SRMF-250',title='Inject traffic externally');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-249',title='Inject traffic internally');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-243',title='AHP:LSS POD');e.save();e.tags.add(AHP)
    e=Epic(key='SRMF-237',title='AHP:CLP POD');e.save();e.tags.add(AHP)
    e=Epic(key='SRMF-231',title='AHP:Admin Portal POD');e.save();e.tags.add(AHP)
    e=Epic(key='SRMF-225',title='AHP:Data Management POD');e.save();e.tags.add(AHP)
    e=Epic(key='SRMF-219',title='AHP:Booking POD');e.save();e.tags.add(AHP)
    e=Epic(key='SRMF-213',title='AHP:Shopping POD');e.save();e.tags.add(AHP)
    e=Epic(key='SRMF-201',title='This Epic is meant to track all the improvements to be addressed');e.save();e.tags.add(ACS)
    e=Epic(key='SRMF-152',title='Pre-requisite for ACS');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-137',title='Have a proper way to manage configuration specific to a given system');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-136',title='Fallback a configuration change');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-135',title='Apply a configuration change');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-134',title='Hardcode clean-up');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-129',title='Validation of Adding/removing VMs from Couchbase cluser');e.save();e.tags.add(ACS_12)
    e=Epic(key='SRMF-128',title='Test application and fallback of couchbase releases');e.save();e.tags.add(ACS_12)
    e=Epic(key='SRMF-118',title='Recover the GQS node');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-85',title='Couchbase Backup');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-82',title='Fail-Over the Oracle instance');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-75',title='Check the health status of a Couchbase Cluster');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-74',title='Check the health status of an Oracle Cluster');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-73',title='Check the health status of the DataCenter');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-72',title='Check the health status of functional queues (LQS/GQS)');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-55',title='Administrate applications queues (LQS/GQS)');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-52',title='Create an Oracle Cluster');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-49',title='Create a couchbase cluster');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-37',title='Initialize a new Datacenter');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-36',title='Dismantle an existing Isolation Zone');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-35',title='Create a new Isolation Zone');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-34',title='Dismantle an existing POD');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-33',title='Deploy a new version of an existing POD');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-20',title='Alerting on environment issues');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-17',title='Display the topology of a DataCenters');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-10',title='Post incident investigation');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-3',title='Apply and fallback Bootstrap releases');e.save();e.tags.add(ACS_11)
    e=Epic(key='SRMF-2',title='Create a new instance of ACS');e.save();e.tags.add(ACS_10)
    e=Epic(key='SRMF-1',title='Creation of a new POD');e.save();e.tags.add(ACS_10)


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_auto_20150921_1328'),
    ]

    operations = [
                  migrations.RunPython(import_epics),
    ]
