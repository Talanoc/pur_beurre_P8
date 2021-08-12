from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    code = models.BigIntegerField(unique=True)
    url = models.URLField()
    product_name = models.CharField(max_length=200)
    nutriscore_grade = models.CharField(max_length=2)
    image_url = models.URLField()
    image_small_url = models.URLField()
    categories = models.ManyToManyField(Category)

    def __str__(self):

        return self.code, self.url, self.product_name, self.nutriscore_grade, self.image_url, self.image_small_url, self.categories


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.product, self.user
