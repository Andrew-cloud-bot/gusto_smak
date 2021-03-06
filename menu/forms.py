from django import forms
from .models import Category, Dish, Anons


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Назва категорії', 'required': 'required'}))
    category_order = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'Порядок у меню', 'required': 'required'}))
    is_visible = forms.BooleanField(initial=True, required=False, widget=forms.CheckboxInput(
        attrs={'placeholder': 'Відображати у меню'}))

    class Meta():
        model = Category
        fields = ('title', 'category_order', 'is_visible')


class DishForm(forms.ModelForm):
    title = forms.CharField(max_length=25, widget=forms.TextInput(
        attrs={'placeholder': 'Назва блюда', 'required': 'required'}))
    price = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'Ціна', 'required': 'required'}))
    category = forms.ModelChoiceField(queryset=Category.objects, required=True)
    photo = forms.ImageField(widget=forms.ClearableFileInput())
    description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'placeholder': 'Опис блюда'}))
    special = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'placeholder': 'Спеціальні пропозиції'}))

    class Meta():
        model = Dish
        fields = ('title', 'price', 'category', 'photo', 'description', 'special')


class AnonsForm(forms.ModelForm):
    title = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs={'placeholder': 'Назва анонсу', 'required': 'required'}))
    photo_sm = forms.ImageField(widget=forms.ClearableFileInput())
    photo_bg = forms.ImageField(widget=forms.ClearableFileInput())
    description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'placeholder': 'Опис анонсу'}))
    is_visible = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'placeholder': 'Відображати анонс'}))

    class Meta():
        model = Anons
        fields = ('title', 'photo_sm', 'photo_bg', 'description', 'is_visible')