from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contacts
def index(request):
    ##return HttpResponse('Главнаястраница')
    content = ['content']
    context = content
    return render(request, template_name='index/index.html',)
def contacts(request):
    list_contacts = Contacts.objects.all()
    content = {
        'contacts_info': list_contacts,
        'title': 'Список новостей'
    }
    ##return HttpResponse('Главнаястраница')
    # content = ['content']
    # context = content
    return render(request, template_name='index/contacts.html', context=content)