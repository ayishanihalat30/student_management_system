# Generated by Django 3.2.4 on 2021-06-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_rename_count_answer_details_number_of_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer_details',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]
