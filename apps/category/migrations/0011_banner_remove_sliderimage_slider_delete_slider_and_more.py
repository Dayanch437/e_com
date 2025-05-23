# Generated by Django 5.1.6 on 2025-04-26 17:21

import apps.utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0010_alter_sliderimage_slider"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "image",
                    apps.utils.fields.CompressedImageField(
                        blank=True, null=True, upload_to="banner"
                    ),
                ),
            ],
            options={
                "verbose_name": "banner",
                "verbose_name_plural": "banners",
            },
        ),
        migrations.RemoveField(
            model_name="sliderimage",
            name="slider",
        ),
        migrations.DeleteModel(
            name="Slider",
        ),
        migrations.DeleteModel(
            name="SliderImage",
        ),
    ]
