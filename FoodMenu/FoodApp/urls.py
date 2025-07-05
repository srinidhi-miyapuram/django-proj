from django.urls import path
from FoodApp import views

urlpatterns = [
    path('', views.index),
    path('items', views.items_ls),
]

