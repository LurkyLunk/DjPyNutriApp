from django.contrib import admin
from .models import FoodItem, DailyLog

admin.site.register(FoodItem)
admin.site.register(DailyLog)

