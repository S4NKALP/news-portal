from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from .serializers import *
from .models import News, Category, SubCategory, Advertisement, Organization


class NewsListView(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.objects.all().order_by("-created_at")
        category = self.request.query_params.get("category", None)
        subcategory = self.request.query_params.get("subcategory", None)

        if category:
            queryset = queryset.filter(
                Q(category__name__iexact=category) | Q(category__id=category)
            )

        if subcategory:
            queryset = queryset.filter(sub_category_id=subcategory)

        return queryset


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "id"


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.prefetch_related("subcategories")
    serializer_class = CategoryListSerializer


class SubCategoryListView(generics.ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        queryset = SubCategory.objects.all()
        category_id = self.request.query_params.get("category", None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class AdvertisementListView(generics.ListAPIView):
    queryset = Advertisement.objects.filter(is_active=True)
    serializer_class = AdvertisementSerializer


class OrganizationListView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
