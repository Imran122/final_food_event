# Generated by Django 2.2.17 on 2021-01-18 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DayNeeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('date', models.CharField(blank=True, max_length=255)),
                ('mealCount', models.IntegerField()),
                ('status', models.CharField(choices=[('rest', 'Rest'), ('easy', 'Easy'), ('workout', 'Workout'), ('all_out', 'All_Out')], default='rest', max_length=32)),
                ('calorieNeed', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('meal1Carbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal1Protein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal1Fat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal1Calories', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal2Carbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal2Protein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal2Fat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal2Calories', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal3Carbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal3Protein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal3Fat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('meal3Calories', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('snackCalories', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('snackCarbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('snackFat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('snackProtein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('totalCarbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('totalFat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('totalProtein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenBreakfast', models.IntegerField(blank=True, null=True)),
                ('chosenBreakfastProtein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenBreakfastCarbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenBreakfastFat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenLunch', models.IntegerField(blank=True, null=True)),
                ('chosenLunchProtein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenLunchCarbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenLunchFat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenDinner', models.IntegerField(blank=True, null=True)),
                ('chosenDinnerProtein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenDinnerCarbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenDinnerFat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenSnack', models.IntegerField(blank=True, null=True)),
                ('chosenSnackProtein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenSnackCarbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosenSnackFat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DayOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('date', models.CharField(blank=True, max_length=255)),
                ('meal1', models.CharField(blank=True, max_length=255)),
                ('meal2', models.CharField(blank=True, max_length=255)),
                ('meal3', models.CharField(blank=True, max_length=255)),
                ('title1', models.CharField(blank=True, max_length=255)),
                ('title2', models.CharField(blank=True, max_length=255)),
                ('title3', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spoonId', models.IntegerField(blank=True)),
                ('original', models.CharField(blank=True, max_length=255)),
                ('originalName', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('amount', models.CharField(blank=True, max_length=255)),
                ('unit', models.CharField(blank=True, max_length=255)),
                ('unitShort', models.CharField(blank=True, max_length=255)),
                ('unitLong', models.CharField(blank=True, max_length=255)),
                ('estimatedCostValue', models.CharField(blank=True, max_length=255)),
                ('estimatedCostUnit', models.CharField(blank=True, max_length=255)),
                ('consistency', models.CharField(blank=True, max_length=255)),
                ('shoppingListUnits', models.CharField(blank=True, max_length=255)),
                ('aisle', models.CharField(blank=True, max_length=255)),
                ('image', models.CharField(blank=True, max_length=255)),
                ('percentProtein', models.CharField(blank=True, max_length=255)),
                ('percentFat', models.CharField(blank=True, max_length=255)),
                ('percentCarbs', models.CharField(blank=True, max_length=255)),
                ('weightPerServing', models.CharField(blank=True, max_length=255)),
                ('unitPerServing', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spoonId', models.CharField(max_length=255)),
                ('imageType', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('readyInMinutes', models.CharField(max_length=255)),
                ('servings', models.CharField(max_length=255)),
                ('sourceUrl', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spoonid', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('imageType', models.CharField(max_length=255)),
                ('servings', models.CharField(max_length=255)),
                ('readyInMinutes', models.CharField(max_length=255)),
                ('spoonlicense', models.CharField(max_length=255)),
                ('sourceName', models.CharField(max_length=255)),
                ('sourceUrl', models.CharField(max_length=255)),
                ('spoonSourceUrl', models.CharField(max_length=255)),
                ('aggregateLikes', models.CharField(max_length=255)),
                ('healthScore', models.CharField(max_length=255)),
                ('spoonScore', models.CharField(max_length=255)),
                ('pricePerServing', models.CharField(max_length=255)),
                ('cheap', models.CharField(max_length=255)),
                ('creditsText', models.CharField(max_length=255)),
                ('cuisines', models.CharField(max_length=255)),
                ('dairyFree', models.CharField(max_length=255)),
                ('diets', models.CharField(max_length=255)),
                ('glutenFree', models.CharField(max_length=255)),
                ('ketogenic', models.CharField(max_length=255)),
                ('lowFodMap', models.CharField(max_length=255)),
                ('sustainable', models.CharField(max_length=255)),
                ('vegan', models.CharField(max_length=255)),
                ('vegetarian', models.CharField(max_length=255)),
                ('veryHealthy', models.CharField(max_length=255)),
                ('veryPopular', models.CharField(max_length=255)),
                ('whole30', models.CharField(max_length=255)),
                ('weightWatchersPoints', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WeekPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day1', to='core.DayNeeds')),
                ('day2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day2', to='core.DayNeeds')),
                ('day3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day3', to='core.DayNeeds')),
                ('day4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day4', to='core.DayNeeds')),
                ('day5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day5', to='core.DayNeeds')),
                ('day6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day6', to='core.DayNeeds')),
                ('day7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day7', to='core.DayNeeds')),
            ],
        ),
        migrations.CreateModel(
            name='UserWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weightLbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('weightKgs', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserNeeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weightLbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('weightKgs', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('dailyProteinPerKg', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('dailyCarbPerKg', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('dailyFatPerKg', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('dailyProteinNeed', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('dailyCarbsNeed', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('dailyFatNeed', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MealPlanDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('date', models.CharField(blank=True, max_length=255)),
                ('meals', models.ManyToManyField(to='core.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stepNumber', models.IntegerField(blank=True)),
                ('stepTitle', models.TextField(blank=True, max_length=1000)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='InstructionIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spoonId', models.IntegerField(blank=True)),
                ('image', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('instruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='InstructionEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spoonId', models.IntegerField(blank=True)),
                ('image', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('instruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('amount', models.CharField(blank=True, max_length=255)),
                ('unit', models.CharField(blank=True, max_length=255)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientNutrients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('amount', models.CharField(blank=True, max_length=255)),
                ('unit', models.CharField(blank=True, max_length=255)),
                ('percentOfDailyNeeds', models.CharField(blank=True, max_length=255)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='DayMealOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.IntegerField(blank=True, default=1)),
                ('optionId', models.CharField(max_length=255)),
                ('optionTitle', models.CharField(max_length=255)),
                ('optionImage', models.CharField(max_length=255)),
                ('optionFat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('optionCarbs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('optionProtein', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('chosen', models.CharField(blank=True, max_length=255, null=True)),
                ('dayNeeds', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='core.DayNeeds')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]