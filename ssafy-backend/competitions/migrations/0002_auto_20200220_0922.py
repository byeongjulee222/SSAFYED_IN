# Generated by Django 2.2.10 on 2020-02-20 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='company_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='population',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='qualitification',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='region',
            field=models.TextField(blank=True),
        ),
    ]
