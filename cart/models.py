from django.contrib.auth.models import User
from django.db import models
import datetime
from store.models import Product
# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product

    @property
    def get_cart_total_price(self):
        order_products =self.orderitem_set.all()
        total_price = sum(product.get_total_price for product in order_products)
        return total_price

    @property
    def get_cart_total_quantity(self):
        order_products =self.orderitem_set.all()
        total_quantity = len(order_products)
        return total_quantity


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product.name} {self.quantity}'

    @property
    def get_total_price(self):
        total_price = self.quantity * self.product.price
        return total_price

