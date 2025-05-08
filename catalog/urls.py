from django.urls import path
from catalog.views import home, contacts, product_detail

app_name = 'catalog'

urlpatterns = [
    path('home/', home),
    path('contacts/', contacts),
    path('product_detail/<int:product_id>', product_detail, name='product_detail'),
]