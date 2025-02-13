from django.db import models
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Sub Categories"


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="news")
    description = models.TextField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "News"


class Advertisement(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    img = models.ImageField(upload_to="advertisement")
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "ads"

