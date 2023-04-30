from os import path

from django.db import models


def upload_to(instance, filename):
    _name, extension = path.splitext(filename)
    return f'products/images/{str(instance.pk)}{extension}'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True
    )
    #image = models.ImageField(upload_to)
    sku = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

