from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('update_user/', update_user, name='update_user'),
    path('update_password/', update_password, name='update_password'),
    path('product/<int:pk>', product, name='product'),
    path('category/<str:foo>', category, name='category'),
    path('category_summary/', category_summary, name='category_summary'),
    path('discount/', discount, name='discount'),
    path('discount_list/', discount_list, name='discount_list'),
    path('books/', books, name='books'),
    path('books/<str:language>/', books_by_language, name='books_by_language'),
    path('books-list/', books_list, name='books_list'),
    path('like/<int:product_id>/', toggle_like, name='toggle_like'),
    path('liked-products/<int:user_id>', liked_products, name='liked_products'),
    path('checkout/', checkout, name='checkout'),
]
