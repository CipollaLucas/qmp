# Generated by Django 4.2.4 on 2024-01-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_pulicado_post_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(related_name='get_posts', to='blog.categoria', verbose_name='Categorías'),
        ),
    ]
