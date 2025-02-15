from app_club.models import Club, ClubSocialLinks
from app_home.models import SocialLink


def social_links(request):
    main_social_link_inst = SocialLink.objects.filter(link_type='inst').first()
    main_social_link_phone = SocialLink.objects.filter(link_type='phone').first()
    main_social_link_tg = SocialLink.objects.filter(link_type='tg').first()
    main_social_link_tiktok = SocialLink.objects.filter(link_type='tik-tok').first()

    return {
        "main_social_link_inst": main_social_link_inst.link_url if main_social_link_inst else None,
        "main_social_link_phone": main_social_link_phone.link_url if main_social_link_phone else None,
        "main_social_link_tg": main_social_link_tg.link_url if main_social_link_tg else None,
        "main_social_link_tiktok": main_social_link_tiktok.link_url if main_social_link_tiktok else None,
    }