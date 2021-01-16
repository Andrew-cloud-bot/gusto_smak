from django.urls import path
from .views import *

urlpatterns = [
    # path('', get_anons_page),
    path('<int:anons_id>/', get_anons_info_page),
    ]