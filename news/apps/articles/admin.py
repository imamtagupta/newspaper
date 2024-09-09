from django.contrib import admin

from apps.articles.models import Article, Author, Category

# Register your models here.

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Category)