from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_home.urls')),
    path('club/', include('app_club.urls')),
    path('news/', include('app_news.urls')),
    path('tinymce/', include('tinymce.urls')),
]

handler404 = 'app_home.views.custom_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)