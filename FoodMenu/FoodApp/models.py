from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

class CustomStorage(FileSystemStorage):
    def get_valid_name(self, name):
        return name

class FoodItem(models.Model):
    item_choices = [("veg","Veg"),("non-veg","Non-Veg")]
    item_types = [("dessert", "Dessert"),("breakfast", "Breakfast"), ("snacks", "Snacks"), ("rice","Rice")]
    img_name = models.ImageField(upload_to="items/",null=False, storage=CustomStorage())
    price = models.IntegerField(default=50,null=False)
    food_type = models.CharField(max_length=20,choices=item_choices,null=False)
    name = models.CharField(max_length=50,null=False, unique=True)
    item_type = models.CharField(max_length=20,choices=item_types,null=False,default="Breakfast")
    description = models.CharField(max_length=100,null=False)
    rating = models.DecimalField(max_digits=2,max_length=5,null=False,decimal_places=1,default=0)


    def __str__(self):
        return self.name


class WallPaper(models.Model):
    img_name = models.ImageField(upload_to="wallpaper/", null=False, storage=CustomStorage())
    name= models.CharField(unique=True,null=False,max_length=20)

    def __str__(self):
        return self.name
    