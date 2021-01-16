from django.shortcuts import render
from .models import Dish, Category, Anons
from django.http import HttpResponse
from .forms import CategoryForm, DishForm, AnonsForm
from django.contrib import messages
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from braces.views import GroupRequiredMixin
from django.core.paginator import Paginator


# Create your views here.

def get_dish_page(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    context = {'title': 'Кафе Смак - Страви',
               'dish': dish,
               }
    return render(request, 'dish.html', context=context)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Category addition success</h1>')
    else:
        form = CategoryForm()
        return render(request, 'add_category.html', context={'form': form})


def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Dish addition success</h1>')
    else:
        form = DishForm()
        return render(request, 'add_dish.html', context={'form': form})


def is_member(user):
    return user.groups.filter(name='manager').exists() or user.is_staff


@login_required(login_url='/login/')
@user_passes_test(is_member)
def categories(request):
    items = Category.objects.all().order_by('category_order')
    paginator = Paginator(items, 4)
    page = request.GET.get('page')
    items = paginator.get_page((page))
    return render(request, 'categories_view.html/', context={'items': items})


@login_required(login_url='/login/')
@user_passes_test(is_member)
def dishes(request):
    items = Dish.objects.all().order_by('category_id')
    paginator = Paginator(items, 4)
    page = request.GET.get('page')
    items = paginator.get_page((page))
    return render(request, 'dishes_view.html', context={'items': items})

@login_required(login_url='/login/')
@user_passes_test(is_member)
def anons(request):
    items = Anons.objects.all().order_by('id')
    paginator = Paginator(items, 4)
    page = request.GET.get('page')
    items = paginator.get_page((page))
    return render(request, 'anons_view.html', context={'items': items})

class CategoryUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('menu:categories')
    success_message = 'Категорія успішно відкоригована!'


class CategoryAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('menu:categories')
    success_message = 'Категорія успішно створена!'


class CategoryDeleteView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Category
    success_url = reverse_lazy('menu:categories')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категорія успішно видалена!')
        return self.post(request, *args, **kwargs)


class DishUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Dish
    form_class = DishForm
    template_name = 'dish_update.html'
    success_url = reverse_lazy('menu:dishes')
    success_message = 'Страва успішно відкоригована!'


class DishAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Dish
    form_class = DishForm
    template_name = 'dish_add.html'
    success_url = reverse_lazy('menu:dishes')
    success_message = 'Страва успішно створена!'


class DishDeleteView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Dish
    success_url = reverse_lazy('menu:dishes')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Страва успішно видалена!')
        return self.post(request, *args, **kwargs)

class AnonsUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Anons
    form_class = AnonsForm
    template_name = 'anons_update.html'
    success_url = reverse_lazy('menu:anons')
    success_message = 'Анонс успішно відкориговано!'


class AnonsAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Anons
    form_class = AnonsForm
    template_name = 'anons_add.html'
    success_url = reverse_lazy('menu:anons')
    success_message = 'Анонс успішно створено!'


class AnonsDeleteView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Anons
    success_url = reverse_lazy('menu:anons')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Анонс успішно видалено!')
        return self.post(request, *args, **kwargs)
