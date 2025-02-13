from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, NewsViewSet, AdvertisementViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'news', NewsViewSet)
router.register(r'advertisements', AdvertisementViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
