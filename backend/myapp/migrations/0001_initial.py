# Generated by Django 5.0.3 on 2024-06-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingName', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('startTime', models.TimeField()),
                ('endDate', models.DateField()),
                ('endTime', models.TimeField()),
                ('applyDate', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('details', models.TextField()),
                ('categories', models.JSONField()),
            ],
        ),
    ]
