from django.db import models
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Categories'

class SubCagtegory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Sub Categories'

class News(models.Model):
    pass