from django.shortcuts import render
from .models import FoodItem, WallPaper

# Create your views here.
def index(request):
    data = get_wallpaper("wallpaper2")
    item_names = ['burger', 'pie']
    items = get_items(item_names)

    return render(request, "index.html", {
        "data": data,
        'items':items,
    })


def get_data():
    data = FoodItem.objects.all()
    
    return data


def get_item(item):
    item = item.capitalize()
    data = FoodItem.objects.filter(name=item)
    # print(data[1],"======================")
    return data


def get_wallpaper(page):
    data = WallPaper.objects.filter(name=page)
    return data

def get_items(lis):
    arr = []
    for item in lis:
        item = item.capitalize()
        data = FoodItem.objects.filter(name=item)
        # print(data[1],"=====================")
        arr.append(data)
    # print(arr[0], " ==================")
    
    return arr
