# Generated by Django 4.2.4 on 2024-06-09 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_profile_name_profile_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='surname',
        ),
    ]
