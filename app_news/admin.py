from django.contrib import admin
from app_news.forms import NewsForm
from app_news.models import News, NewsPictures


class NewsPicturesInline(admin.TabularInline):
    model = NewsPictures
    extra = 1
    verbose_name = "Доп. картинка новости"
    verbose_name_plural = "Доп. картинки новости"



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    form = NewsForm

    inlines = [NewsPicturesInline]


