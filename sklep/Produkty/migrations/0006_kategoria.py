# Generated by Django 4.0.3 on 2022-05-27 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0005_produkty_producent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
    ]
