# Generated by Django 3.0 on 2020-02-13 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200213_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='jobs_deadline',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='jobs_qualification',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='jobs_salary',
        ),
    ]
