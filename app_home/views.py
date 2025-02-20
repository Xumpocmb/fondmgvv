from django.shortcuts import render

from app_club.models import ClubRegion, Club
from app_news.models import News


def index(request):
    club_regions = ClubRegion.objects.all()
    all_clubs = Club.objects.all()
    all_news = News.objects.all()
    context = {
        'all_clubs': all_clubs,
        'club_regions': club_regions,
        'all_news': all_news
    }
    return render(request, 'app_home/index.html', context)


def get_document(request):
    return render(request, 'app_home/document.html')

def custom_404_view(request, exception):
    return render(request, 'app_home/404.html')