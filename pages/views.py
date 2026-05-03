from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import FeedbackForm, PluginForm, RegisterForm
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

@login_required
def account(request):
    return render(request, 'pages/account.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            return redirect('home')

    else:
        form = FeedbackForm()

    return render(request, 'pages/contact.html', {'form': form})

@login_required
def plugin_create(request):
    if request.method == 'POST':
        form = PluginForm(request.POST, request.FILES)

        if form.is_valid():
            plugin = form.save(commit=False)
            plugin.author = request.user
            plugin.save()
            return redirect(plugin.get_absolute_url())

    else:
        form = PluginForm()

    return render(request, 'pages/form.html', {
        'form': form,
        'title': 'Добавить плагин'
    })

@login_required
def plugin_update(request, pk):
    plugin = get_object_or_404(Plugin, pk=pk)

    if request.method == 'POST':
        form = PluginForm(request.POST, request.FILES, instance=plugin)

        if form.is_valid():
            form.save()
            return redirect(plugin.get_absolute_url())

    else:
        form = PluginForm(instance=plugin)

    return render(request, 'pages/form.html', {
        'form': form,
        'title': 'Редактировать плагин'
    })

@login_required
def plugin_delete(request, pk):
    plugin = get_object_or_404(Plugin, pk=pk)

    if request.method == 'POST':
        plugin.delete()
        return redirect('home')

    return render(request, 'pages/detail.html', {
        'plugin': plugin,
        'show_delete_modal': True,
    })