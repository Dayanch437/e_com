# Generated by Django 5.1.6 on 2025-05-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0011_banner_remove_sliderimage_slider_delete_slider_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="banner",
            name="description",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
