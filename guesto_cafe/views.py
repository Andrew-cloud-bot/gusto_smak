from django.http import HttpResponse
from django.shortcuts import render, redirect
from menu.models import Category, Dish
from random import randint
from .settings import GALLERY
from contact_info.forms import UserMessagesForm


def get_main_page(request):
    specials = []
    gallery = []
    rnd = []
    form = UserMessagesForm()

    if request.method == 'POST':
        form = UserMessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/#contact')

    categories = Category.objects.filter(is_visible=True).order_by('category_order')

    for item in categories:
        item.dishes = Dish.objects.filter(category=item.id)

    dishes = Dish.objects.all()
    for dish in dishes:
        if dish.special:
            specials.append(dish)

    while len(set(rnd)) < GALLERY:
        rnd.append(randint(0, len(dishes)-1))

    for i in set(rnd):
        gallery.append(dishes[i].photo.url)

    context = {'title': 'Кафе Смак',
               'about_title': 'Наша історія',
               'about_info_1':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sed dapibus leo nec ornare diam.'
                            ' Sed commodo nibh ante facilisis bibendum dolor feugiat at. Duis sed dapibus leo nec ornare.',
               'team_title':'Зустрічайте шефа',
               'team_info_1':'За гастрономічні враження відповідає шеф-кухар Остап Бендер. У меню представлені різноманітні європейські страви, як традиційні, так і авторські. '
                             'Також наш шеф спільно з метрдотелем можуть скласти індивідуальне меню по вашим бажанням, додавши в нього улюблені вами страви.',
               'team_info_2':'Колекція вин ресторану «Смак» налічує близько 120 позицій. Від всесвітньо відомих винних будинків до невеликих сімейних виноробства.'
                             ' Коктейльне меню - це ще одна особливість нашого ресторану.',
               'menu_title': 'Меню',
               'specials':specials,
               'gallery':gallery,
               'categories':categories,
               'form':form,
               }
    return render(request, 'index.html', context=context)