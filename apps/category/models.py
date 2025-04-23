from django.db import models
from apps.utils.fields import  CompressedImageField


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True, blank=True)
    image = CompressedImageField(upload_to="product/images",null=True, blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

