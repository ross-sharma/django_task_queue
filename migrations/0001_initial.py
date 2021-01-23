# Generated by Django 3.1.3 on 2021-01-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('last_attempt_datetime', models.DateTimeField(db_index=True, null=True)),
                ('lock_id', models.CharField(blank=True, max_length=64)),
                ('queue_class_name', models.CharField(db_index=True, max_length=256)),
                ('data_json', models.TextField(default='null')),
                ('last_error', models.TextField(blank=True)),
                ('tag', models.CharField(db_index=True, max_length=128)),
                ('error_count', models.IntegerField(default=0)),
                ('retry_allowed', models.BooleanField(db_index=True, default=True)),
                ('max_attempts', models.IntegerField(default=5)),
                ('priority', models.IntegerField(default=100)),
            ],
        ),
    ]
