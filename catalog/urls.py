from django.urls import path
from catalog.views import ProductsListView, ProductDetailView, ContactsTemplateView

app_name = 'catalog'

urlpatterns = [
    # path('home/', home, name='home'),
    path('home/', ProductsListView.as_view(), name='home'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    # path('contacts/', contacts, name='contacts'),
    # path('product_detail/<int:product_id>', product_detail, name='product_detail'),
]