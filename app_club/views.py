from django.shortcuts import render, get_object_or_404
from app_club.models import Club


def club_info(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    club_social_link_inst = club.social_links.filter(link_type='inst').first()
    club_social_link_phone = club.social_links.filter(link_type='phone').first()
    club_social_link_tg = club.social_links.filter(link_type='tg').first()
    club_social_link_tiktok = club.social_links.filter(link_type='tik-tok').first()

    context = {
        "club": club,
        "club_social_link_inst": club_social_link_inst.social_link if club_social_link_inst else None,
        "club_social_link_phone": club_social_link_phone.social_link if club_social_link_phone else None,
        "club_social_link_tg": club_social_link_tg.social_link if club_social_link_tg else None,
        "club_social_link_tiktok": club_social_link_tiktok.social_link if club_social_link_tiktok else None,
    }
    return render(request, 'app_club/club.html', context)
