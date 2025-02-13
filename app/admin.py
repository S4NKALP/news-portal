from django.contrib import admin
from .models import Category, SubCagtegory, News, Advertisement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("-id",)

@admin.register(SubCagtegory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    search_fields = ("name",)
    ordering = ("-id",)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "img", "description")
    search_fields = ("title",)
    ordering = ("-id",)

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active", "img", "link")
    search_fields = ("link",)
    ordering = ("-id",)
