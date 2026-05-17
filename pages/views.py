from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import FeedbackForm, PluginForm, RegisterForm, CommentForm
from .models import Plugin, Tag, Comment

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
    form = CommentForm()

    return render(request, 'pages/detail.html', {
        'plugin': plugin,
        'form': form
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
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при регистрации. Проверьте поля формы.')
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
            form.save_m2m()
            messages.success(request, 'Плагин успешно добавлен!')
            return redirect(plugin.get_absolute_url())
        else:
            messages.error(request, 'Ошибка при добавлении плагина. Проверьте поля формы.')

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
            messages.success(request, 'Плагин успешно обновлен!')
            return redirect(plugin.get_absolute_url())
        else:
            messages.error(request, 'Ошибка при обновлении плагина. Проверьте поля формы.')

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
        messages.success(request, 'Плагин успешно удален!')
        return redirect('home')

    return render(request, 'pages/detail.html', {
        'plugin': plugin,
        'show_delete_modal': True,
    })

def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    items = tag.plugins.all()

    context = {
        'title': f'Плагины с тегом: {tag.name}',
        'tag': tag,
        'items': items
    }

    return render(request, 'pages/index.html', context)

@login_required
def add_comment(request, pk):
    plugin = get_object_or_404(Plugin, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = plugin
            comment.save()
            messages.success(request, 'Комментарий успешно добавлен!')
        else:
            messages.error(request, 'Ошибка при добавлении комментария.')
    
    return redirect('plugin_detail', pk=pk)