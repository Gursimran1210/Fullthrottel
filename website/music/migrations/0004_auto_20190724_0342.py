# Generated by Django 2.2.2 on 2019-07-23 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190724_0252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gurdasmaan',
            old_name='album',
            new_name='album_title',
        ),
        migrations.RemoveField(
            model_name='album',
            name='album_logo',
        ),
        migrations.RemoveField(
            model_name='album',
            name='album_title',
        ),
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
    ]
