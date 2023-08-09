from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)

class DailyLog(models.Model):
    date = models.DateField(auto_now_add=True)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
