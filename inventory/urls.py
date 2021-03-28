from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_form/', views.add_product, name='add_product'),
    path('products/', views.get_all_products, name='get_products'),
    path('categories/', views.get_all_catgories, name='get_categories'),
    path('categories/<int:category_id>/', views.get_category_products, name='get_category_products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]
