from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore

from product.models import Product


class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
