import os

from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from app_club.models import ClubCity, ClubRegion, generate_unique_filename, compress_image


def news_main_photos_path(instance, filename):
    return generate_unique_filename(instance, filename, 'news_main_photos')


def news_other_photos_path(instance, filename):
    return generate_unique_filename(instance, filename, 'news_other_photos')


class News(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст", blank=True, null=True)
    main_picture = models.ImageField(upload_to=news_main_photos_path, blank=True, null=True,
                                     verbose_name="Главная картинка новости")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original = News.objects.get(pk=self.pk)
            if original.main_picture != self.main_picture and self.main_picture.size > 1 * 1024 * 1024:
                self.main_picture = compress_image(self.main_picture)
        else:
            if self.main_picture and self.main_picture.size > 1 * 1024 * 1024:
                self.main_picture = compress_image(self.main_picture)

        super(News, self).save(*args, **kwargs)


class NewsPictures(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='other_pictures', verbose_name="Новость")
    img = models.ImageField(upload_to=news_other_photos_path, blank=True, null=True,
                            verbose_name="Доп. картинки новости")

    def __str__(self):
        return f"Доп. картинка для новости: {self.news.title}"

    class Meta:
        verbose_name = 'Дополнительная картинка новости'
        verbose_name_plural = 'Дополнительные картинки новостей'

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original = NewsPictures.objects.get(pk=self.pk)
            if original.img != self.img and self.img.size > 1 * 1024 * 1024:
                self.img = compress_image(self.img)
        else:
            if self.img and self.img.size > 1 * 1024 * 1024:
                self.img = compress_image(self.img)

        super(NewsPictures, self).save(*args, **kwargs)


@receiver(post_delete, sender=NewsPictures)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(pre_save, sender=News)
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
            old_instance = News.objects.get(pk=instance.pk)
            if old_instance.main_picture and old_instance.main_picture != instance.main_picture:
                if os.path.isfile(old_instance.main_picture.path):
                    os.remove(old_instance.main_picture.path)
        except News.DoesNotExist:
            pass


@receiver(post_delete, sender=News)
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
