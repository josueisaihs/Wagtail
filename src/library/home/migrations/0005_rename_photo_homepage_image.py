# Generated by Django 4.1.7 on 2023-04-17 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_image_homepage_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='photo',
            new_name='image',
        ),
    ]
