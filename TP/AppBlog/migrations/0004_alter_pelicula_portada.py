# Generated by Django 4.1.3 on 2022-12-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0003_pelicula_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='media/imagenes/portadas'),
        ),
    ]
