# Generated by Django 2.2.17 on 2021-03-24 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20210324_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='mealPosition',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('morning snack', 'Morning Snack'), ('lunch', 'Lunch'), ('afternoon snack', 'Afternoon Snack'), ('dinner', 'Dinner'), ('evening snack', 'Evening Snack')], default='breakfast', max_length=255),
        ),
    ]