from django.contrib import admin
from .models import Category, SubCategory, News, Advertisement, Organization, NewsImage


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "email", "phone_no", "logo")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    search_fields = ("name",)
    ordering = ("id",)


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInline]
    list_display = ("id", "title", "description")
    search_fields = ("title",)
    ordering = ("id",)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active", "img", "link")
    search_fields = ("link",)
    ordering = ("id",)
