from django import forms
from django.forms import ModelForm
from .models import ProductCategory, Product

class ProductForm(ModelForm):
    category = forms.ModelChoiceField(
        required = False,
        queryset = ProductCategory.objects.all(),
        
    )
    class Meta:
        model = Product
        fields = '__all__'

class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'
