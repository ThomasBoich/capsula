from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import News, Category


## СОЗДАЁМ СТРАНИЦУ НОВОСТИ
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


## СОЗДАЁМ СТРАНИЦУ ОПРЕДЕЛЁННОЙ КАТЕГОРИИ
def get_category(request, category_id):
    '''СОЗДАЁМ СТРАНИЦУ ОПРЕДЕЛЁННОЙ КАТЕГОРИИ НОВОСТЕЙ ПО URL ЗАПРОСУ'''

    ## получаем новости из определенной категории по ID категории из запроса
    news = News.objects.filter(category_id=category_id)
    ## получаем список всех категорий
    category = Category.objects.all()
    ## получаем определенную категорию по её ID
    category_key = Category.objects.get(pk=category_id)
    
    return render(request, 'news/category.html',
                  {'news': news, 'categories': category, 'category_key': category_key, 'category': category, })
