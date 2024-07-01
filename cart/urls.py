from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('to-cart/<int:product_id>/<str:action>', views.to_cart, name='to_cart'),
]
