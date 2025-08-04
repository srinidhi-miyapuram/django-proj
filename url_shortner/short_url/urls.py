from django.urls import path
from short_url import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_url>', views.redirect_to_original_url, name='new_url')
]
