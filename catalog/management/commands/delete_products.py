from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    Product.objects.all().delete()
    Category.objects.all().delete()

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('All data has been deleted!'))
