from django.urls import path
from FoodApp import views

urlpatterns = [
    path('', views.index),
]

