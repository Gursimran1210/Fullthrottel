# Generated by Django 2.2.2 on 2019-07-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190717_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(default='', max_length=50)),
                ('Email', models.CharField(default='', max_length=50)),
                ('Comment', models.CharField(max_length=5000)),
            ],
        ),
    ]
