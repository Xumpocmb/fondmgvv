from django.contrib import admin
from app_home.models import ERIP_link, PhoneNumber, QRCode, SiteEmail, SocialLink

admin.site.register(ERIP_link)
admin.site.register(PhoneNumber)
admin.site.register(QRCode)
admin.site.register(SiteEmail)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('link_name', 'link_url')
    prepopulated_fields = {"link_slug": ("link_name",)}