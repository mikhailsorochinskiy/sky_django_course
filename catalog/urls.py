from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.views import ProductsListView, ProductDetailView, ContactsTemplateView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductsByCategoryView

app_name = 'catalog'

urlpatterns = [
    # path('home/', home, name='home'),
    path('home/', ProductsListView.as_view(), name='home'),
    path('product_detail/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    # path('<str:category>', ProductsCategoryListView.as_view(), name='products_category'),
    path('products/category/<int:category_id>', ProductsByCategoryView.as_view(), name='products_category'),
    # path('contacts/', contacts, name='contacts'),
    # path('product_detail/<int:product_id>', product_detail, name='product_detail'),
]