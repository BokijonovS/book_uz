# store/templatetags/store_tags.py
from django import template

from cart.models import OrderItem
from store.models import Category, LikeDislike

register = template.Library()

@register.simple_tag
def get_all_categories():
    return Category.objects.all()


@register.simple_tag
def likes_count():
    likes = LikeDislike.objects.all()
    return likes.count()


@register.simple_tag
def order_items_count():
    order_items = OrderItem.objects.all()
    return order_items.count()