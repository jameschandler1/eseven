from django.db import models
import os
# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('static', str(instance.id), filename)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to=get_image_path)
    price = models.FloatField()
    
class Order(models.Model):
    transaction_id = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=255, null=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product_title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    code = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




