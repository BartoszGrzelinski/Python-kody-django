# Generated by Django 4.0.3 on 2022-06-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0007_produkty_kategoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='przeznaczenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kto', models.CharField(max_length=100)),
            ],
        ),
    ]
