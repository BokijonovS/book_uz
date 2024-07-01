from django.contrib import admin

from store.models import Category, Author, Product, Publisher, Cover, Translater


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Product)
admin.site.register(Publisher)
admin.site.register(Cover)
admin.site.register(Translater)
