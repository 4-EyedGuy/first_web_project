from django.contrib import admin
from .models import Plugin

@admin.register(Plugin)
class PluginAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price', 'created_at')
    list_select_related = ('author',)