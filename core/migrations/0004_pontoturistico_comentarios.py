# Generated by Django 4.2.5 on 2023-09-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0003_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.comentario'),
        ),
    ]
