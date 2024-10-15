from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test students to the database'

    Product.objects.all().delete()
    Category.objects.all().delete()

    def handle(self, *args, **kwargs):

        fruit, _ = Category.objects.get_or_create(name='Фрукты')
        vegetables, _ = Category.objects.get_or_create(name='Овощи')
        cereals, _ = Category.objects.get_or_create(name='Крупы')
        preserves, _ = Category.objects.get_or_create(name='Консервы')

        products = [
            {'name': 'Яблоки', 'price': '150', 'category': fruit},
            {'name': 'Апельсины', 'price': '200', 'category': fruit},
            {'name': 'Мандарины', 'price': '220', 'category': fruit},
            {'name': 'Картофель', 'price': '50', 'category': vegetables},
            {'name': 'Капуста', 'price': '60', 'category': vegetables},
            {'name': 'Гречка', 'price': '80', 'category': cereals},
            {'name': 'Рис', 'price': '110', 'category': cereals},
            {'name': 'Тушенка', 'price': '200', 'category': preserves},
            {'name': 'Килька в томатном соусе', 'price': '120', 'category': preserves},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.name}'))
