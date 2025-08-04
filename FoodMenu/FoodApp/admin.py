from django.contrib import admin
from .models import FoodItem, WallPaper, UserCartItems

# Register your models here.
admin.site.register(FoodItem)
admin.site.register(WallPaper)
admin.site.register(UserCartItems)