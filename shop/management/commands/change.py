import random
import decimal

from django.db.models.signals import post_save
from django.core.management.base import BaseCommand

from shop.models import Product


class Command(BaseCommand):
    """
    Example: ./python manage.py change.py
    """
    help = 'Change Product price, status and remains'

    def handle(self, *args, **options):
        products = Product.objects.all()
        for i in products:
            i.price = float(decimal.Decimal(random.randrange(100000) / 100))
            i.status = random.choice(['in_stock', 'out_of_stock'])
            i.remains = random.randrange(1000)
        Product.objects.bulk_update(products, ['price', 'status', 'remains'])
        post_save.send(products[0].__class__, instance=products[0], created=True)
