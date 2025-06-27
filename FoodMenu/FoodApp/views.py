from django.shortcuts import render
from .models import FoodItem, WallPaper

# Create your views here.
def index(request):
    data = get_wallpaper()
    return render(request, "index.html", {
        "data": data,
    })


def get_data():
    data = FoodItem.objects.all()
    
    return data


def get_item(item):
    item = item.capitalize()
    print(item, " ==================")
    data = FoodItem.objects.filter(name=item)
    return data


def get_wallpaper():
    data = WallPaper.objects.all()
    return data