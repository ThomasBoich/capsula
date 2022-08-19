from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import News


def news(request):
    # return HttpResponse('Страница Новостей')
    list_news = News.objects.order_by('-created_att')
    content = {
        'news': list_news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=content)
