from django.shortcuts import render, get_object_or_404
from .models import Plugin

def index(request):
    items = Plugin.objects.all()

    context = {
        'title': 'Всё нужное для начинающих композиторов',
        'welcome_text': 'Здесь вы найдете все необходимые ресурсы для начала вашего пути в мире музыки',
        'items': items
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def plugin_detail(request, pk):
    plugin = get_object_or_404(Plugin, pk=pk)

    return render(request, 'pages/detail.html', {
        'plugin': plugin
    })