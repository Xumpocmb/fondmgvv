from django.urls import path
from app_news.views import get_news

app_name = 'app_news'

urlpatterns = [
    path('<int:news_id>/', get_news, name='news'),
]