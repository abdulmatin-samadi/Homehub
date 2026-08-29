"""
HomeHub loyihasining bosh URL konfiguratsiyasi.
Har bir app o'z urls.py fayliga ega va shu yerga include qilinadi.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('elonlar/', include('properties.urls', namespace='properties')),
    path('sevimlilar/', include('favorites.urls', namespace='favorites')),
    path('sharhlar/', include('reviews.urls', namespace='reviews')),
    path('xabarlar/', include('chat.urls', namespace='chat')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('api/', include('api.urls', namespace='api')),
    path('', include('pages.urls', namespace='pages')),
]

# Development rejimida media fayllarni (avatar, rasmlar) xizmat qilish
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
