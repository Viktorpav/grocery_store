from django.db import models
from food.models import Product

from PIL import Image


class Status(models.Model):
    name = models.CharField(max_length=48, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Status %s" % self.name

    # class Meta:
    #     order_name = "Status"
    #     order_name_plural = "Statuses orders"


class Order(models.Model):
    customer_name = models.CharField(max_length=128)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    comments = models.TextField(max_length=250, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order %s %s" % (self.id, self.status.name)

    # class Meta:
    #     order_name = "Order"
    #     order_name_plural = "Orders"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    # class Meta:
    #     order_name = "Product"
    #     order_name_plural = "Products"

