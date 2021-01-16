from django.shortcuts import render
from menu.models import Anons
# Create your views here.

def get_anons_info_page(request, anons_id):
    anons_list = []

    anons = Anons.objects.get(id=anons_id)
    # for anons in anonses:
    #     anons_list.append(anons)

    context = {'title': 'Анонси Смаку',
               'anons': anons,
               }
    return render(request, 'anons_info.html', context=context)

