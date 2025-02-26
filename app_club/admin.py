from django.contrib import admin

from app_club.forms import ClubForm
from app_club.models import Club, ClubPictures, ClubSocialLinks, ClubRegion, ClubCity


class ClubSocialLinksInline(admin.StackedInline):
    model = ClubSocialLinks
    extra = 1
    verbose_name = "Контакт клуба"
    verbose_name_plural = "Контакты клуба"
    can_delete = True

class ClubPicturesInline(admin.TabularInline):
    model = ClubPictures
    extra = 1
    verbose_name = "Картинка клуба"
    verbose_name_plural = "Картинки клуба"

class ClubAdmin(admin.ModelAdmin):
    inlines = [ClubSocialLinksInline, ClubPicturesInline]
    list_filter = ('city', 'region', 'date_of_founding')
    form = ClubForm




admin.site.register(Club, ClubAdmin)
admin.site.register(ClubRegion)
admin.site.register(ClubCity)


