# Generated by Django 4.0.6 on 2022-07-18 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_journal', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
    ]
