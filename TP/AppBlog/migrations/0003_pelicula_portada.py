# Generated by Django 4.1.3 on 2022-12-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portadas'),
        ),
    ]
