from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProductForm
from .models import Product,ProductCategory
from django.views.generic import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html')

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory/')
        
    else:
        form = ProductForm()

    return render(request, 'inventory/product_form.html', {'form': form})


def get_all_products(request):
    products = Product.objects.all()
    print(1)
    return render(request, 'inventory/all_products.html', {'products': products})

def get_all_catgories(request):
    categories = ProductCategory.objects.all()
    return render(request, 'inventory/all_categories.html', {'categories': categories})

def get_category_products(request, category_id):
    # products = Product.objects.filter(category=category)
    category = ProductCategory.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    print(products)

    context = {
        'category' : category,
        'products' : products
    }

    return render(request, 'inventory/category_products.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'inventory/product_detail.html', {'product':product})

@api_view(['GET'])
def detailView(request, product_id):
    product = Product.objects.get(id=product_id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)




class AddProdcutView(View):
    def get(self, request):
        form = ProductForm()
        context = {'form': form}
        return render(request, 'inventory/product_form.html', context)

    def post(self, request):
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inventory/')
        
        context = {'form': form}

        return render(request, 'inventory/prodcut_fomr.html', context)


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List': '/product-list',
        'Create': '/product-create/',
        'Detail View': '/task-detail/<str:pk>/'
    }

    return Response(api_urls)

@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many= True)
    return Response(serializer.data)
