# Generated by Django 3.2.8 on 2021-11-07 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='mesage',
            new_name='message',
        ),
    ]
