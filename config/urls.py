from django.contrib import admin
from django.urls import path
from pages.views import index, about, plugin_detail, contact, plugin_create, plugin_update, plugin_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('plugin/<int:pk>/', plugin_detail, name='plugin_detail'),
    path('plugin/add/', plugin_create, name='plugin_create'),
    path('plugin/<int:pk>/edit/', plugin_update, name='plugin_update'),
    path('plugin/<int:pk>/delete/', plugin_delete, name='plugin_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)