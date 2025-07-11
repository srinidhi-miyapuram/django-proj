from django.urls import path, reverse_lazy, re_path
from FoodApp import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_page, name='login'),

    path('register', views.register_page),
    path('items', views.items_ls, name='items'),
    # path('sort_items', views.sort_items),
]

