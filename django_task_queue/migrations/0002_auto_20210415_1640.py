# Generated by Django 3.1.5 on 2021-04-15 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_task_queue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='max_attempts',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(),
        ),
    ]
