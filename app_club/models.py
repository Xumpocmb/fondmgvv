from django.db import models


class ClubCity(models.Model):
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")

    class Meta:
        db_table = 'club_city'
        verbose_name = 'Город клуба'
        verbose_name_plural = 'Города клубов'

    def __str__(self):
        return f"Город клуба: {self.city}"


class ClubRegion(models.Model):
    region = models.CharField(max_length=100, blank=True, null=True, verbose_name="Область")

    class Meta:
        db_table = 'club_region'
        verbose_name = 'Область клуба'
        verbose_name_plural = 'Области клубов'

    def __str__(self):
        return f"Область клуба: {self.region}"


class Club(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название клуба")
    description = models.TextField(max_length=4500, blank=True, null=True, verbose_name="Описание клуба")
    military_unit = models.CharField(max_length=100, blank=True, null=True, verbose_name="Воинская часть")
    date_of_founding = models.DateField(blank=True, null=True, verbose_name="Дата основания клуба")
    city = models.ForeignKey(ClubCity, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Город")
    region = models.ForeignKey(ClubRegion, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Область")
    main_picture = models.ImageField(upload_to='club_main_photos/', blank=True, null=True, verbose_name="Главная картинка клуба")

    class Meta:
        db_table = 'club'
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'

    def __str__(self):
        return f"Клуб: {self.name}"


class ClubSocialLinks(models.Model):
    TYPE_SOCIAL_CHOICES = [
        ('phone', 'Телефон'),
        ('inst', 'Instagram'),
        ('tg', 'Telegram'),
        ('tik-tok', 'TikTok'),
    ]
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='social_links', verbose_name="Клуб")
    link_type = models.CharField(max_length=100, choices=TYPE_SOCIAL_CHOICES, verbose_name="Тип контакта", blank=True, null=True)
    social_link = models.CharField(max_length=100, blank=True, null=True, verbose_name="Контакт")

    class Meta:
        db_table = 'club_social_links'
        verbose_name = 'Контакт клуба'
        verbose_name_plural = 'Контакты клуба'

    def __str__(self):
        return f"Контакт: {self.id}"


class ClubPictures(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='other_pictures', verbose_name="Клуб")
    img = models.ImageField(upload_to='club_other_photos/', blank=True, null=True, verbose_name="Картинки клуба")

    class Meta:
        db_table = 'club_pictures'
        verbose_name = 'Картинка клуба'
        verbose_name_plural = 'Картинки клубов'

    def __str__(self):
        return f"Картинка для клуба: {self.club.name}"