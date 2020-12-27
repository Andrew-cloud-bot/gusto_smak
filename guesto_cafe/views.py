from django.http import HttpResponse
from django.shortcuts import render
from menu.models import Category, Dish

def get_main_page(request):
    category = Category.objects.all().order_by('category_order')
    dish = Dish.objects.all().order_by('category_id')

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
               'categories':category,
               'dishes':dish
               }
    return render(request, 'index.html', context=context)