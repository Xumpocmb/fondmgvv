from django.shortcuts import render

from app_club.models import ClubRegion, Club


def index(request):
    club_regions = ClubRegion.objects.all()
    all_clubs = Club.objects.all()
    context = {
        'all_clubs': all_clubs,
        'club_regions': club_regions
    }
    return render(request, 'app_home/index.html', context)


def get_document(request):
    return render(request, 'app_home/document.html')