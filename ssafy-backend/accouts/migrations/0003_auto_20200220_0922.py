# Generated by Django 2.2.10 on 2020-02-20 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accouts', '0002_auto_20200218_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.TextField(blank=True, default='no'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.TextField(blank=True, null=True),
        ),
    ]
