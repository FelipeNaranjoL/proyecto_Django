# Generated by Django 4.0.5 on 2022-06-15 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pag_perros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimento',
            name='imagen',
            field=models.ImageField(null=True, upload_to='alimentos'),
        ),
        migrations.AddField(
            model_name='juguete',
            name='imagen',
            field=models.ImageField(null=True, upload_to='juguetes'),
        ),
    ]
