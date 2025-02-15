from django.shortcuts import render
from app_club.models import Club


def club_info(request, club_id):
    try:
        club = Club.objects.get(id=club_id)
    except Club.DoesNotExist:
        club = None

    club_social_link_inst = club.social_links.filter(link_type='inst').first()
    club_social_link_phone = club.social_links.filter(link_type='phone').first()
    club_social_link_tg = club.social_links.filter(link_type='tg').first()
    club_social_link_tiktok = club.social_links.filter(link_type='tik-tok').first()

    context = {
        "club": club,
        "club_social_link_inst": club_social_link_inst,
        "club_social_link_phone": club_social_link_phone,
        "club_social_link_tg": club_social_link_tg,
        "club_social_link_tiktok": club_social_link_tiktok
    }
    return render(request, 'app_club/club.html', context)
