from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache


class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(unique=True, max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=15, choices=[('in_stock', 'In stock'), ('out_of_stock', 'Out of stock')])
    remains = models.IntegerField()

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def clear_cache(sender, instance, **kwargs):
    cache.clear()

# Create your models here.
