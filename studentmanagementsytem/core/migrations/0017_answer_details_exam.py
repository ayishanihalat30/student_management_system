# Generated by Django 3.2.4 on 2021-06-16 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_count_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer_details',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.exam'),
        ),
    ]
