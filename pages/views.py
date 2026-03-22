from django.shortcuts import render

def index(request):
    context = {
        'title': 'Всё нужное для начинающих композиторов',
        'welcome_text': 'Здесь вы найдете все необходимые ресурсы для начала вашего пути в мире музыки'
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')