# Generated by Django 3.2.4 on 2021-06-15 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_main_subject_subject_model_subject_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subject',
            new_name='Allotted_Subject',
        ),
    ]
