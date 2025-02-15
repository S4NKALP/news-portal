# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news-list'),
    path('news/<int:id>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('subcategories/', views.SubCategoryListView.as_view(), name='subcategory-list'),
    path('advertisements/', views.AdvertisementListView.as_view(), name='advertisement-list'),
    path('organization/', views.OrganizationListView.as_view(), name='organization-list'),
]