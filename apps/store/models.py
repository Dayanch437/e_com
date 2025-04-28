from django.db import models

from apps.cart.models import User
from apps.category.models import Category
from apps.utils.fields import CompressedImageField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = CompressedImageField(upload_to="products/images",blank=True, null=True)
    color = CompressedImageField(upload_to="products/images",blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='comments')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text},by {self.user}"


class Image(models.Model):
    image = CompressedImageField(upload_to="products/images", blank=True)
    color_picture = CompressedImageField(upload_to="products/images", blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='pictures',blank=True, null=True)
    class Meta:
        verbose_name_plural = 'images'
        db_table = 'products_images'

    def __str__(self):
        return self.image.name


