# Generated by Django 3.0.5 on 2020-04-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whokillsit', '0006_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='remark',
            name='r_user',
            field=models.CharField(default='Bleurenard', max_length=128),
        ),
    ]
