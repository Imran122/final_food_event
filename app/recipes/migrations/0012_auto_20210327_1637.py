# Generated by Django 2.2.19 on 2021-03-27 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20210327_1314'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='events',
            unique_together={('start', 'mealPosition')},
        ),
    ]