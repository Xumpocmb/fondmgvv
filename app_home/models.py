import os

from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver


class SocialLink(models.Model):
    TYPE_SOCIAL_CHOICES = [
        ('phone', 'Телефон'),
        ('inst', 'Instagram'),
        ('tg', 'Telegram'),
        ('tik-tok', 'TikTok'),
    ]
    link_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название")
    link_type = models.CharField(max_length=100, choices=TYPE_SOCIAL_CHOICES, verbose_name="Тип контакта", blank=True, null=True)
    link_url = models.CharField(max_length=100, blank=True, null=True, verbose_name="Контакт")

    class Meta:
        db_table = 'social_link'
        verbose_name = 'Ссылка на соц. сеть'
        verbose_name_plural = 'Ссылки на соц. сети'

    def __str__(self):
        return f"Ссылка: {self.link_name}"


class SiteEmail(models.Model):
    email_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Название почты")
    email_address = models.CharField(max_length=50, blank=True, null=True, verbose_name="Адрес почты")

    class Meta:
        db_table = 'site_email'
        verbose_name = 'Почта'
        verbose_name_plural = 'Почты'

    def __str__(self):
        return f"Почта: {self.email_name}"


class ERIP_link(models.Model):
    erip_link = models.CharField(max_length=250, blank=True, null=True, verbose_name="Ссылка на ЕРИП")

    class Meta:
        db_table = 'erip_link'
        verbose_name = 'ЕРИП ссылки'
        verbose_name_plural = 'ЕРИП ссылки'

    def __str__(self):
        return f"ЕРИП: {self.erip_link}"


class QRCode(models.Model):
    qr_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название QR кода")
    qr_picture = models.ImageField(upload_to='qr/', blank=True, null=True, verbose_name="QR код")

    class Meta:
        db_table = 'qr_code'
        verbose_name = 'QR код'
        verbose_name_plural = 'QR коды'

    def __str__(self):
        return f"QR код: {self.qr_name}"


@receiver(post_delete, sender=QRCode)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)