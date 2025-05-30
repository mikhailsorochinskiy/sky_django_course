from django.urls import path
from catalog.views import ProductsListView, ProductDetailView, ContactsTemplateView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    # path('home/', home, name='home'),
    path('home/', ProductsListView.as_view(), name='home'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    # path('contacts/', contacts, name='contacts'),
    # path('product_detail/<int:product_id>', product_detail, name='product_detail'),
]