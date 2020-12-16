from django.http import HttpResponse
from django.shortcuts import render

def get_main_page(request):
    context = {'title': 'Кафе Смак',
               'about_title': 'Наша історія'
               }
    return render(request, 'index.html', context=context)