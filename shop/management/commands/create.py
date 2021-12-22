from django.core.management.base import BaseCommand
from shop.models import Category, Product
import random
import string
import decimal


def get_name(max_letters=1, objs=[]):
    def build_name(max_letters=1):
        return random.choice(string.ascii_uppercase) + ''.join(random.choices(
            string.ascii_lowercase, k=random.randrange(max_letters)))

    name = build_name(max_letters)
    while name in [obj.name for obj in objs]:
        name = build_name(max_letters)
    return name


class Command(BaseCommand):
    """
    Example: ./python manage.py create.py __count_categories__ __count_products__
    """
    help = 'Create categories and products'

    def add_arguments(self, parser):
        parser.add_argument('countes', nargs='+', type=str)

    def handle(self, *args, **options):
        categories = []
        products = []
        for i in range(int(options['countes'][0])):
            name = get_name(20)
            while name in [category.name for category in categories]:
                name = get_name(20)
            categories.append(Category(name=get_name(20, categories)))

        for i in range(int(options['countes'][1])):
            products.append(Product(
                name=get_name(20, products),
                category=random.choice(categories),
                price=float(decimal.Decimal(random.randrange(100000) / 100)),
                status=random.choice(['in_stock', 'out_of_stock']),
                remains=random.randrange(1000)

            ))

        Category.objects.bulk_create(categories, ignore_conflicts=False)
        Product.objects.bulk_create(products, ignore_conflicts=False)
