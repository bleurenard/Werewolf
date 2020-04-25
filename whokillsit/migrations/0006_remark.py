# Generated by Django 3.0.5 on 2020-04-23 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whokillsit', '0005_strategy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_content', models.TextField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('s_remark', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='whokillsit.Strategy')),
                ('u_remark', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='whokillsit.UserInfo')),
            ],
        ),
    ]
