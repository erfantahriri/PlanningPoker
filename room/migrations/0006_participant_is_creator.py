# Generated by Django 2.2.1 on 2019-05-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_auto_20190509_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='is_creator',
            field=models.BooleanField(default=False, verbose_name='Is Creator'),
        ),
    ]
