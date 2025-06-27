from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import UserDetails

# Create your views here.
def index(request):
    return HttpResponse("<em>Hello World!</em>")

def help(request):
    my_dict = { "helper": "This is a helper page" }
    return render(request, 'help.html', context=my_dict)

def imagePage(request):
    return render(request, 'imagePage.html')

def usersDetails(request):
    users = UserDetails.objects.all()
    user_details = {'users': users}
    return render(request, 'users.html', context=user_details)