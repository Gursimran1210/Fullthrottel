# Generated by Django 2.2.2 on 2019-07-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20190724_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gurdasmaan',
            name='album',
            field=models.CharField(max_length=200),
        ),
    ]
