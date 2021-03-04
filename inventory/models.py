from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    costing_method = models.CharField(max_length=20)
    parent =  models.IntegerField(null=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    cost_price = models.IntegerField()
    sales_price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, blank=True)
    
