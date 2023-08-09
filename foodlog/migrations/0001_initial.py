# Generated by Django 4.2.4 on 2023-08-09 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('calories', models.IntegerField()),
                ('protein', models.DecimalField(decimal_places=2, max_digits=5)),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fats', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='DailyLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodlog.fooditem')),
            ],
        ),
    ]