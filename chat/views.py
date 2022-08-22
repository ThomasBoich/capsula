from django.shortcuts import render

# Create your views here.
def chat(request):
    ##return HttpResponse('Главнаястраница')
    content = ['content']
    context = content
    return render(request, template_name='chat/index.html',)