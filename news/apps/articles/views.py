from django.shortcuts import render
from .models import Article, Category

# Create your views here.

def articles(request):
    article_data = Article.objects.all().order_by("-published_dt")
    category_data = Category.objects.all()
    return render(request, 'articles/article_list.html', {"articles": article_data, "categories": category_data})

