# Generated by Django 4.0.5 on 2022-06-17 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_score_score_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allotted_subject',
            name='division',
        ),
        migrations.RemoveField(
            model_name='student',
            name='division',
        ),
        migrations.DeleteModel(
            name='Division',
        ),
    ]
