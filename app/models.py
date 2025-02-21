from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Organization(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.IntegerField()
    logo = models.ImageField(upload_to="logo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "org"


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name="subcategories", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Sub Categories"


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, max_length=30000)
    image = models.ImageField(upload_to="news")
    video = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True, blank=True
    )
    is_video = models.BooleanField(default=False)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "News"


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="news/images", blank=True)

    def __str__(self):
        return f"Image for {self.news.title}"


class Advertisement(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    img = models.ImageField(upload_to="advertisement")
    link = models.CharField(max_length=255)
    ads_types = models.CharField(
        choices=[("bannerAds", "bannerAds"), ("sideAds", "sideAds")], max_length=255
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "ads"
