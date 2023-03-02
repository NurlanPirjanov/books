# Generated by Django 4.1.3 on 2022-11-08 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_books_book_number_alter_books_book_url_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='lang',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.booklanguage', verbose_name='Kitob tili'),
        ),
        migrations.AlterField(
            model_name='books',
            name='yunalish',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.qanigelik', verbose_name='Yunalish'),
        ),
    ]