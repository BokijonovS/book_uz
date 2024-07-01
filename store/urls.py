from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('discount/', views.discount, name='discount'),
    path('books/', views.books, name='books'),
    path('books-list/', views.books_list, name='books_list'),
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path('liked-products/<int:user_id>', views.liked_products, name='liked_products'),
]
