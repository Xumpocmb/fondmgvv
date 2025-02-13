from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название клуба")
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Описание клуба")
    military_unit = models.CharField(max_length=100, blank=True, null=True, verbose_name="Воинская часть")
    date_of_founding = models.DateField(blank=True, null=True, verbose_name="Дата основания клуба")
    main_picture = models.ImageField(upload_to='club_main_photos/', blank=True, null=True, verbose_name="Главная картинка клуба")

    class Meta:
        db_table = 'club'
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'

    def __str__(self):
        return f"Клуб: {self.name}"


class ClubSocialLinks(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='social_links', verbose_name="Клуб")
    instagram_link = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ссылка на Intagram")
    telegram_link = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ссылка на Telegram")
    tiktok_link = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ссылка на Tik Tok")


class ClubPictures(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='other_pictures', verbose_name="Клуб")
    img = models.ImageField(upload_to='club_other_photos/', blank=True, null=True, verbose_name="Картинки клуба")

    class Meta:
        db_table = 'club_pictures'
        verbose_name = 'Картинка клуба'
        verbose_name_plural = 'Картинки клубов'

    def __str__(self):
        return f"Картинка для клуба: {self.club.name}"