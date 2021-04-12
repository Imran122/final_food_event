# Generated by Django 2.2.17 on 2021-01-18 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210118_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='d1', to='core.DayNeeds')),
                ('day2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='d2', to='core.DayNeeds')),
                ('day3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='d3', to='core.DayNeeds')),
                ('day4', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='d4', to='core.DayNeeds')),
                ('day5', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='d5', to='core.DayNeeds')),
                ('day6', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='d6', to='core.DayNeeds')),
                ('day7', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='d7', to='core.DayNeeds')),
            ],
        ),
    ]
