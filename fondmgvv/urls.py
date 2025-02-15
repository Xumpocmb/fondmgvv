from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_home.urls')),
    path('club/', include('app_club.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)