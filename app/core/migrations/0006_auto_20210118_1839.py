# Generated by Django 2.2.17 on 2021-01-18 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210118_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daymealoptions',
            name='dayNeeds',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DayNeeds'),
        ),
    ]
