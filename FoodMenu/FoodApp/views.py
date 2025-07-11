from django.shortcuts import render
from .models import FoodItem, WallPaper
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django.core.paginator import Paginator



# Create your views here.
def index(request):
    item_cls = DataItems
    data = item_cls.get_wallpaper()
    item_names = ['burger', 'pie']
    items = item_cls.get_items(item_names)

    return render(request, "index.html", {
        "data": data,
        'items':items,
        'url_contact': "#contact"
    })


@login_required(login_url='login')
def items_ls(request):
    item_cls = DataItems
    items = []
    # Search Item
    if request.method == "GET":
        item_name = request.GET.get('item_name')
        print(item_name, ' ===================')

        if item_name != '' and item_name is not None:
            items.append(item_cls.get_filter_search_item(item_name))
        else:
            items.append(item_cls.get_all_items())
        
        
        
    elif request.method == "POST":
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
        items.append(item_cls.get_filter_items(data['food_type'], data['item_type']))
    

    # Pagination
    paginator = Paginator(items[0],4)
    page = request.GET.get('page')
    items = [paginator.get_page(page)]

    return render(request, 'items.html', {
        'items': items,
        'url_contact': '/',
    })




def login_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        passwd = request.POST.get("passwd")

        user = authenticate(username=name, password=passwd)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('items'))
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse("User Not Found")
    else:
        return render(request, 'login.html', {
            'url_contact': '/',
        })

def register_page(request):
    registered = False
    if request.method == "POST":
        password = request.POST.get('password1')
        user = UserForm(request.POST)
        if user.is_valid():
            user_commit = user.save(commit=False)
            user_commit.set_password(password)
            user.save()
            registered = True
            return HttpResponseRedirect('/')
        else:
            return HttpResponse(user.errors)
    else:
        user = UserForm()
        return render(request,'register.html', {
            'user_form': user,
            'registered':registered,
            'url_contact': '/',
        })

class DataItems:

  
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
    

    def get_filter_search_item(item_name):
        item_name = item_name.capitalize()
        return FoodItem.objects.filter(name__icontains=item_name)

    def get_filter_items(food_type, item_type):
        # Here __in will loop through all the list elements and gives us the output
        if len(food_type) > 0 and len(item_type) > 0:
            return FoodItem.objects.filter(food_type__in=food_type,item_type__in=item_type)
        elif len(food_type) > 0:
            return FoodItem.objects.filter(food_type__in=food_type)
        elif len(item_type) > 0:
            return FoodItem.objects.filter(item_type__in=item_type)
        