from rest_framework import serializers
from .models import Category, SubCategory, News, Advertisement


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"
        depth = 2
class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"
