from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_form/', views.AddProdcutView.as_view(), name='add_product'),
    path('products/', views.get_all_products, name='get_products'),
    path('categories/', views.get_all_catgories, name='get_categories'),
    path('categories/<int:category_id>/', views.get_category_products, name='get_category_products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category_form', views.AddProductCategoryView.as_view(), name='add_category'),
    path('api/', views.apiOverView, name='api'),
    path('api/product-list', views.productList, name='productList'),
    path('api/detail-view/<int:product_id>', views.detailView, name='detailView'),
    path('api/create-view/', views.createView, name='createView'),

]
