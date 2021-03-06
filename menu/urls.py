from django.urls import path
from .views import *

urlpatterns = [
    path('<int:dish_id>/', get_dish_page),
    # path('add_category/', add_category, name='add_category'),
    # path('add_dish/', add_dish, name='add_dish'),
    path('<int:dish_id>/', get_dish_page),

    path('categories/', categories, name='categories'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='categories_update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='categories_delete'),
    path('categories/add', CategoryAddView.as_view(), name='categories_add'),

    path('dishes/', dishes, name='dishes'),
    path('dishes/update/<int:pk>/', DishUpdateView.as_view(), name='dishes_update'),
    path('dishes/delete/<int:pk>/', DishDeleteView.as_view(), name='dishes_delete'),
    path('dishes/add', DishAddView.as_view(), name='dishes_add'),

    path('anons/', anons, name='anons'),
    path('anons/update/<int:pk>/', AnonsUpdateView.as_view(), name='anons_update'),
    path('anons/delete/<int:pk>/', AnonsDeleteView.as_view(), name='anons_delete'),
    path('anons/add', AnonsAddView.as_view(), name='anons_add'),
    ]
