from django.contrib import admin
from django.db import models
from django.forms import Textarea
from tinymce.widgets import TinyMCE

from app_news.forms import NewsForm
from app_news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')

    form = NewsForm
