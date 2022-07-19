# Generated by Django 4.0.6 on 2022-07-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('roast', models.CharField(default='', max_length=50)),
                ('origin', models.CharField(default='', max_length=50)),
                ('notes', models.TextField()),
                ('brew_method', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('fav_roast', models.CharField(choices=[('dark', 'DARK'), ('medium', 'MEDIUM'), ('light', 'LIGHT')], default='Medium', max_length=6)),
                ('brew_method', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
