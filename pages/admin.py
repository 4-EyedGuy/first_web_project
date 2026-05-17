from django.contrib import admin
from .models import Plugin, Tag, Comment

@admin.register(Plugin)
class PluginAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price', 'created_at')
    list_select_related = ('author',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    list_select_related = ('author', 'post')
    readonly_fields = ('created_at',)