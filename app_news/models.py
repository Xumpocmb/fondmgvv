from django.db import models

from app_club.models import ClubCity, ClubRegion


class News(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
