# Generated by Django 2.2.2 on 2019-07-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Comment',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Last_name',
            field=models.CharField(max_length=50),
        ),
    ]
