# Generated by Django 4.0.5 on 2022-06-18 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_academic_year_remove_answer_details_answer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='allotted_subject',
            name='photo',
        ),
        migrations.AddField(
            model_name='allotted_subject',
            name='academic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.academic_year'),
        ),
        migrations.AddField(
            model_name='allotted_subject',
            name='subject_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.subject_code'),
        ),
    ]