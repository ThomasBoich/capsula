from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import News, Category

def news(request):
    # return HttpResponse('Страница Новостей')
    # list_news = News.objects.order_by('-created_att')
    # categories = Category.objects.all()
    # content = {
    #     'news': list_news,
    #     'title': 'Список новостей',
    #     'category': categories,
    # }
    # return render(request, template_name='news/index.html', context=content)
    news = News.objects.all()
    category = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': category,
       }
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.all()
    category_key = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': category, 'category_key': category_key, 'category': category,})
