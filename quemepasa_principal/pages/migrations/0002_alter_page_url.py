# Generated by Django 4.2.4 on 2024-01-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.SlugField(max_length=128, unique=True),
        ),
    ]
