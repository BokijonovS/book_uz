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
    path('category/<slug:category_slug>', category, name='category'),
    path('category_summary/', category_summary, name='category_summary'),
    path('discount/', discount, name='discount'),
    path('discount_list/', discount_list, name='discount_list'),
    path('books/', books, name='books'),
    path('books/lang/<slug:language_slug>/', books_by_language, name='books_by_language'),
    path('books/yr/<slug:year_slug>/', books_by_year, name='books_by_year'),
    path('books/order/date/', books_by_date, name='books_by_date'),
    path('books/order/rating/', books_by_rating, name='books_by_rating'),
    path('books/order/popuarity/', books_by_popularity, name='books_by_popularity'),
    path('books/order/<int:number>/', books_in_page, name='books_in_page'),
    path('books-list/', books_list, name='books_list'),
    path('like/<int:product_id>/', toggle_like, name='toggle_like'),
    path('liked-products/<int:user_id>', liked_products, name='liked_products'),
    path('checkout/', checkout, name='checkout'),
]
