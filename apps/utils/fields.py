import os
import uuid
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.fields.files import FieldFile
from imagekit import ImageSpec
from PIL import Image, UnidentifiedImageError
from django.core.files.uploadedfile import TemporaryUploadedFile


def upload_file(instance: TemporaryUploadedFile, filename: str) -> str:
    path = type(instance).__name__.lower()

    filename, ext = filename.rsplit(".", 1)
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join(path, filename)


class CompressedImageSpec(ImageSpec):
    format = "WEBP"
    options = {"quality": 75}


class CompressedImageFile(FieldFile):
    def save(self, name, content, save=True):
        from django.db.models import Model
        import os
        try:
            if not (name.endswith(".gif") or name.endswith(".svg")):
                content.seek(0)
                image = Image.open(content)
                image_format = CompressedImageSpec.format

                compressed_image = ContentFile(b"")
                image.save(compressed_image, format=image_format, quality=75)

                base_name, _ = os.path.splitext(name)
                name = f"{base_name}.{image_format.lower()}"
                compressed_image.seek(0)

                # DELETE OLD FILE IF UPDATING
                if hasattr(self.instance, 'pk') and self.instance.pk:
                    field_name = self.field.name
                    model = self.instance.__class__
                    try:
                        old_file = model.objects.get(pk=self.instance.pk).__dict__[field_name]
                        if old_file and old_file != self.name:
                            full_path = os.path.join(self.storage.location, old_file)
                            if os.path.isfile(full_path):
                                os.remove(full_path)
                    except model.DoesNotExist:
                        pass

                return super().save(name, compressed_image, save)

        except UnidentifiedImageError:
            pass

        return super().save(name, content, save)


class CompressedMixin:
    attr_class = CompressedImageFile

    def __init__(self, upload_to=upload_file, **kwargs):
        super().__init__(upload_to=upload_to, **kwargs)


class CompressedFileField(CompressedMixin, models.FileField):
    pass


class CompressedImageField(CompressedMixin, models.ImageField):
    pass


