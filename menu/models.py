from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)
    category_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Dish(models.Model):
    title = models.CharField(max_length=25, unique=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


