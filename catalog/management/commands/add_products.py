from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test products'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='категория1')

        products = [
            {'name': 'продукт1', 'price': 100, 'category': category},
            {'name': 'продукт2', 'price': 200, 'category': category},
            {'name': 'продукт3', 'price': 300, 'category': category}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.name}'))
