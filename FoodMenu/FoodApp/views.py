from django.shortcuts import render
from django.core.serializers import serialize
from .models import FoodItem, WallPaper
import json

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
    items = [item_cls.get_all_items()]
    return render(request, "items.html", {
        "items": items,
    })

def sort_items(request):
    items_ls = DataItems
    data = {}
    data['food_type'] = []
    data['item_type'] = []
    # Checking what are the choices user made
    if request.POST.getlist('non-veg'):
        data['food_type'].append('non-veg')
    if request.POST.getlist('veg'):
        data['food_type'].append('veg')
    if request.POST.getlist('dessert'):
        data['item_type'].append('dessert')
    if request.POST.getlist('rice'):
        data['item_type'].append('rice')
    if request.POST.getlist('snacks'):
        data['item_type'].append('snacks')
    if request.POST.getlist('breakfast'):
        data['item_type'].append('breakfast')
    items = [items_ls.get_filter_items(data['food_type'], data['item_type'])]
    
    return render(request, 'items.html', {
        'items': items
    })

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request,'register.html')

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
    
  

    def get_filter_items(food_type, item_type):
        # Here __in will loop through all the list elements and gives us the output
        if len(food_type) > 0 and len(item_type) > 0:
            return FoodItem.objects.filter(food_type__in=food_type,item_type__in=item_type)
        elif len(food_type) > 0:
            return FoodItem.objects.filter(food_type__in=food_type)
        elif len(item_type) > 0:
            return FoodItem.objects.filter(item_type__in=item_type)
        