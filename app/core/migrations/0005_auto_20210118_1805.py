# Generated by Django 2.2.17 on 2021-01-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210118_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayneeds',
            name='meal1Chosen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dayneeds',
            name='meal2Chosen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dayneeds',
            name='meal3Chosen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dayneeds',
            name='meal4Chosen',
            field=models.BooleanField(default=False),
        ),
    ]