# Generated by Django 4.0.4 on 2022-04-14 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder_app', '0002_reminderlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReminderList',
        ),
    ]