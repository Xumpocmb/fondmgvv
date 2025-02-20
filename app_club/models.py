import os
import re

from PIL import Image
import io
from django.core.files.base import ContentFile

from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from unidecode import unidecode


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

def compress_image(image, quality=85, max_size=(800, 800)):
    """
    Сжимает изображение до заданного качества и размера.

    :param image: Исходное изображение.
    :param quality: Качество сжатия (1-100).
    :param max_size: Максимальный размер изображения (ширина, высота).
    :return: Сжатое изображение.
    """
    img = Image.open(image)

    # Изменяем размер изображения, если оно превышает максимальные размеры
    img.thumbnail(max_size)

    # Сохраняем изображение в буфер с заданным качеством
    output = io.BytesIO()
    img.save(output, format='JPEG', quality=quality)
    output.seek(0)

    # Возвращаем сжатое изображение
    return ContentFile(output.getvalue(), name=image.name)


def generate_unique_filename(instance, filename, folder_name):
    name, ext = os.path.splitext(filename)
    name = unidecode(name)
    new_name = slugify(name)
    new_name = re.sub(r'[^a-zA-Z0-9_]', '', new_name)
    return f"{folder_name}/{new_name}{ext}"


def club_main_photos_path(instance, filename):
    return generate_unique_filename(instance, filename, 'club_main_photos')

def club_other_photos_path(instance, filename):
    return generate_unique_filename(instance, filename, 'club_other_photos')

class Club(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название клуба")
    description = models.TextField(max_length=4500, blank=True, null=True, verbose_name="Описание клуба")
    military_unit = models.CharField(max_length=100, blank=True, null=True, verbose_name="Воинская часть")
    date_of_founding = models.DateField(blank=True, null=True, verbose_name="Дата основания клуба")
    city = models.ForeignKey(ClubCity, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Город")
    region = models.ForeignKey(ClubRegion, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Область")
    main_picture = models.ImageField(upload_to=club_main_photos_path, blank=True, null=True,
                                     verbose_name="Главная картинка клуба")

    class Meta:
        db_table = 'club'
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'

    def __str__(self):
        return f"Клуб: {self.name}"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original = Club.objects.get(pk=self.pk)
            if original.main_picture != self.main_picture and self.main_picture.size > 1 * 1024 * 1024:
                self.main_picture = compress_image(self.main_picture)
        else:
            if self.main_picture and self.main_picture.size > 1 * 1024 * 1024:
                self.main_picture = compress_image(self.main_picture)

        super(Club, self).save(*args, **kwargs)





class ClubSocialLinks(models.Model):
    TYPE_SOCIAL_CHOICES = [
        ('phone', 'Телефон'),
        ('inst', 'Instagram'),
        ('tg', 'Telegram'),
        ('tik-tok', 'TikTok'),
    ]
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='social_links', verbose_name="Клуб")
    link_type = models.CharField(max_length=100, choices=TYPE_SOCIAL_CHOICES, verbose_name="Тип контакта", blank=True,
                                 null=True)
    social_link = models.CharField(max_length=100, blank=True, null=True, verbose_name="Контакт")

    class Meta:
        db_table = 'club_social_links'
        verbose_name = 'Контакт клуба'
        verbose_name_plural = 'Контакты клуба'

    def __str__(self):
        return f"Контакт: {self.id}"


class ClubPictures(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='other_pictures', verbose_name="Клуб")
    img = models.ImageField(upload_to=club_other_photos_path, blank=True, null=True, verbose_name="Картинки клуба")

    class Meta:
        db_table = 'club_pictures'
        verbose_name = 'Картинка клуба'
        verbose_name_plural = 'Картинки клубов'

    def __str__(self):
        return f"Картинка для клуба: {self.club.name}"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original = ClubPictures.objects.get(pk=self.pk)
            if original.img != self.img and self.img.size > 1 * 1024 * 1024:
                self.img = compress_image(self.img)
        else:
            if self.img and self.img.size > 1 * 1024 * 1024:
                self.img = compress_image(self.img)

        super(ClubPictures, self).save(*args, **kwargs)


@receiver(post_delete, sender=ClubPictures)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(pre_save, sender=Club)
def delete_old_main_picture(sender, instance, **kwargs):
    """
    Этот сигнал вызывается перед сохранением объекта. В обработчике сигнала мы проверяем, существует ли уже сохраненное изображение, и если оно отличается от нового, удаляем старый файл.
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    if instance.pk:
        try:
            old_instance = Club.objects.get(pk=instance.pk)
            if old_instance.main_picture and old_instance.main_picture != instance.main_picture:
                if os.path.isfile(old_instance.main_picture.path):
                    os.remove(old_instance.main_picture.path)
        except Club.DoesNotExist:
            pass


@receiver(post_delete, sender=Club)
def delete_main_picture_on_delete(sender, instance, **kwargs):
    """
    Этот сигнал вызывается после удаления объекта. В обработчике сигнала мы удаляем файл изображения, если объект удален.
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    # Удаляем файл при удалении объекта
    if instance.main_picture:
        if os.path.isfile(instance.main_picture.path):
            os.remove(instance.main_picture.path)