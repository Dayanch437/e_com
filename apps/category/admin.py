from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.category.models import Category,Banner
from apps.store.models import Product,Comments,Image  # Adjust import if needed
class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 0
    readonly_fields = ('user', 'text', 'created_date', 'modified_date')

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ProductAdmin(ImportExportModelAdmin):  # Enables import/export
    list_display = ('name', 'price', 'stock', 'is_available', 'category')
    list_filter = ('is_available', 'category')
    search_fields = ('name',)
    inlines = [CommentsInline, ImageInline]

admin.site.register(Product, ProductAdmin)

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

    readonly_fields = ('name', 'price', 'stock', 'is_available', 'created_date', 'modified_date')
    can_delete = False
    show_change_link = True

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ProductInline]



admin.site.register(Category, CategoryAdmin)
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id']
