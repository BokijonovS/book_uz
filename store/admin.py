from django.contrib import admin

from store.models import Category, Author, Product, Publisher, Cover, Translater, Language


admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Cover)
admin.site.register(Translater)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Language)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'pages')
    list_display_links = ('name',)
    list_editable = ('price', 'pages')
    prepopulated_fields = {'slug': ('name',)}




