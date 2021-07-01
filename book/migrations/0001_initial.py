# Generated by Django 3.2.4 on 2021-06-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, verbose_name='Book name')),
                ('book_author', models.CharField(max_length=100, verbose_name='book author')),
                ('publication_year', models.CharField(max_length=4, verbose_name='year of book publication')),
                ('registration_time', models.DateTimeField(auto_now_add=True, verbose_name='book registration time')),
                ('update_time', models.DateTimeField(verbose_name='update time Book information')),
                ('username_register', models.CharField(max_length=50, unique=True, verbose_name='username that registered this book')),
            ],
        ),
    ]