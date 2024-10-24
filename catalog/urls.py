from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDetailView, CategoryDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/new/', CategoryCreateView.as_view(), name='category_new'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('products/new/', ProductCreateView.as_view(), name='product_new'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='products_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]
