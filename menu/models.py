from django.db import models
from os import path
from uuid import uuid4


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)
    category_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Dish(models.Model):

    def get_file_name_dishes(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes/', filename)

    title = models.CharField(max_length=25, unique=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_file_name_dishes)
    description = models.CharField(max_length=300)
    special = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Anons(models.Model):

    def get_file_name_anonses(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/anonses/', filename)

    title = models.CharField(max_length=15, unique=True)
    photo_sm = models.ImageField(upload_to=get_file_name_anonses)
    photo_bg = models.ImageField(upload_to=get_file_name_anonses)
    description = models.CharField(max_length=300)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title
