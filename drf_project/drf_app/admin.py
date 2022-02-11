from django.contrib import admin
from .models import Post, Author, Company, Address, Geo


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'update_date')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'update_date')


@admin.register(Company)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Address)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'suite')


@admin.register(Geo)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('lat', 'lng')
