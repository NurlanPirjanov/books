# Generated by Django 4.1.6 on 2023-02-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_kafedra_books_kafedra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklanguage',
            name='lang',
            field=models.CharField(max_length=200),
        ),
    ]
