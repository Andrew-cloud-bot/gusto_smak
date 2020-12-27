from django.urls import path
from .views import get_dish_page

urlpatterns = [
    path('', get_dish_page)
    ]