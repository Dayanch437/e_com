from django.db import models
from django.db.models import ForeignKey

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


class SliderImage(models.Model):
    image = CompressedImageField(upload_to="product/images",null=True, blank=True)
    slider = models.ForeignKey('category.Slider', on_delete=models.CASCADE,related_name='images')
    def __str__(self):
        return self.image.name


class Slider(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)  # Optional button or redirect
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0,blank=True)  # for manual sorting
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

