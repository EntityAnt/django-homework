from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок блога')
    content = models.TextField(verbose_name='Статья блога')
    preview_image = models.ImageField(upload_to='blog/previews/', blank=True, null=True, verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано!')
    views_counter = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
