from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # @daverobb2011
    class Meta:
        verbose_name_plural = 'Categories'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cover(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Translater(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=17)
    writing = models.CharField(max_length=100)
    year = models.CharField(max_length=2024)
    language = models.CharField(max_length=100)
    pages = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    cover = models.ForeignKey(Cover, on_delete=models.CASCADE)
    translater = models.ForeignKey(Translater, on_delete=models.CASCADE, null=True, blank=True)
    discount = models.DecimalField(default=0, decimal_places=2, max_digits=10, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    # Add Sale Stuff
    is_sale = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class LikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes_dislikes')
    is_like = models.BooleanField(default=True)  # True for like, False for dislike

    def __str__(self):
        return f'{self.product} {self.is_like}'

