# Generated by Django 2.0.5 on 2018-08-08 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='image',
            field=models.ImageField(blank=True, upload_to='mainApp/static/mainApp/img/items', verbose_name='Imagen del articulo'),
        ),
    ]
