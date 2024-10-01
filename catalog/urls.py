from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('products/new/', ProductCreateView.as_view(), name='product_new'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='products_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]
