# Generated by Django 2.2.1 on 2019-05-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_auto_20190518_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='vote_cards_status',
            field=models.CharField(choices=[('hidden', 'hidden'), ('visible', 'visible')], default='hidden', max_length=32, verbose_name='Vote Cards Status'),
        ),
    ]
