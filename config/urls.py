from django.contrib import admin
from django.urls import path
from pages.views import index, about, plugin_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),

    path('plugin/<int:pk>/', plugin_detail, name='plugin_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)