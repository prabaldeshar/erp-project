from django import forms
from .models import ProductCategory

class ProductForm(forms.Form):
    name = forms.CharField(label="Product name", max_length=100)
    cost_price = forms.IntegerField(label="Cost Price")
    sales_price = forms.IntegerField(label="Sales Price")
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all())