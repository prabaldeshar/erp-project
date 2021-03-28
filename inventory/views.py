from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProductForm
from .models import Product,ProductCategory

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html')

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            cost_price = form.cleaned_data['cost_price']
            sales_price = form.cleaned_data['sales_price']
            category = form.cleaned_data['category']
            product = Product(name=name, cost_price=cost_price, sales_price=sales_price, category=category)
            product.save()
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