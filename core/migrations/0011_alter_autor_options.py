# Generated by Django 5.1.7 on 2025-05-16 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_livro_autor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'autores'},
        ),
    ]
