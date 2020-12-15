from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def categories(request):
    items = ['Холодные закуски', 'Основные блюда', 'Напитки', 'Алкоголь']
    res = ''
    for item in items:
        res += f'<div><h2>{item}</h2></div>'
    return HttpResponse(res)