# Generated by Django 5.0.5 on 2024-05-19 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_userprofile_delete_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
