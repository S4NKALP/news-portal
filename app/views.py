from rest_framework import viewsets
from .models import Category, SubCategory, News, Advertisement
from .serializers import CategorySerializer, SubCategorySerializer, NewsSerializer, AdvertisementSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related('subcategories')
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
