from django.contrib import admin
from .models import Comments, Product,Image
from import_export.admin import ImportExportModelAdmin
admin.site.register(Comments)
admin.site.register(Image)
# admin.site.register(Product,ImportExportModelAdmin)