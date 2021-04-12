# Generated by Django 2.2.19 on 2021-03-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_auto_20210327_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='mealPosition',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('morning snack', 'Morning Snack'), ('lunch', 'Lunch'), ('afternoon snack', 'Afternoon Snack'), ('dinner', 'Dinner'), ('evening snack', 'Evening Snack')], max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='events',
            unique_together={('start', 'mealPosition', 'mealChosen')},
        ),
    ]