from django.urls import path
from app_club.views import club_info

app_name = 'app_club'

urlpatterns = [
    path('<int:club_id>/', club_info, name='club_info'),
]