# Generated by Django 4.0.2 on 2022-07-04 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('Edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='')),
                ('tiempo', models.IntegerField()),
            ],
        ),
    ]
