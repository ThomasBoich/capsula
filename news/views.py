from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import News, Category


def news(request):
    # return HttpResponse('Страница Новостей')
    list_news = News.objects.order_by('-created_att')
    categories = Category.objects.all()
    content = {
        'news': list_news,
        'title': 'Список новостей',
        'category': categories,
    }
    return render(request, template_name='news/index.html', context=content)

def get_category(request, get_category_id):

    category = get_category_id
    return render(request, template_name='news/category.html',)
