from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_form/', views.add_product, name='add_product'),
    path('products/', views.get_products, name='get_products')
]
