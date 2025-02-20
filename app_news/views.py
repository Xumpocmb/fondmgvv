from django.shortcuts import render, get_object_or_404

from app_news.models import News


def get_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'app_news/news.html', {'news': news})
