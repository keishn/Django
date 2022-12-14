# Generated by Django 3.2.16 on 2022-12-13 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('address', models.CharField(max_length=100, verbose_name='Адреса')),
                ('text', models.TextField(verbose_name='Опис')),
                ('published', models.DateTimeField()),
                ('price', models.IntegerField(verbose_name='Середній чек, ₴')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
