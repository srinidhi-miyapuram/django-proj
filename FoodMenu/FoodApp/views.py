from django.shortcuts import render
from .models import FoodItem, WallPaper

# Create your views here.
def index(request):
    item_cls = DataItems
    data = item_cls.get_wallpaper()
    item_names = ['burger', 'pie']
    items = item_cls.get_items(item_names)

    return render(request, "index.html", {
        "data": data,
        'items':items,
    })


def items_ls(request):
    item_cls = DataItems
    items = item_cls.get_all_items()
    return render(request, "items.html", {
        "items": items
    })


class DataItems:
    def get_data():
        data = FoodItem.objects.all()
        
        return data


    def get_item(item):
        item = item.capitalize()
        data = FoodItem.objects.filter(name=item)
        return data


    def get_wallpaper():
        data = WallPaper.objects.all()
        return data

    def get_items(lis):
        arr = []
        for item in lis:
            item = item.capitalize()
            data = FoodItem.objects.filter(name=item)
            arr.append(data)
        
        return arr
    
    def get_all_items():
        data = FoodItem.objects.all()
        return data
