# Generated by Django 4.2.5 on 2023-09-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
