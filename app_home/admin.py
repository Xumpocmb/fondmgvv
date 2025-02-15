from django.contrib import admin
from app_home.models import ERIP_link, QRCode, SiteEmail, SocialLink

admin.site.register(ERIP_link)
admin.site.register(QRCode)
admin.site.register(SiteEmail)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('link_name', 'link_url')
