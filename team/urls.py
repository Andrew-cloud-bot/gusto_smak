from django.urls import path
from .views import get_anons_page

urlpatterns = [
    path('', get_anons_page)
    ]