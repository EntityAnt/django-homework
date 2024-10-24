from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите название категории')
    description = models.TextField(verbose_name='Описание категории', help_text='Введите описание категории',
                                   blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Продукт', help_text='Введите название продукта')
    description = models.TextField(max_length=300, verbose_name='Описание', help_text='Введите описание продукта',
                                   blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Фото',
                              help_text='Загрузите фото продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    views_counter = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f'{self.name}'



    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
