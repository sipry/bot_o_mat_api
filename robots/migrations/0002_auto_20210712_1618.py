# Generated by Django 3.2.5 on 2021-07-12 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Robots',
            new_name='Robot',
        ),
        migrations.RenameModel(
            old_name='Types',
            new_name='Type',
        ),
    ]
