from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    top = (
        ('mt-30', 'mt-30'),
        ('mt-85', 'mt-85'),
    )
    name = models.CharField(max_length=300, default=None)
    category_image = models.ImageField(upload_to='category',default=None)
    category_description = models.TextField(default=None,max_length=500)
    margin_top = models.CharField(max_length=100, choices=top, default="mt-30")
    slug = models.SlugField(max_length=100,default=None)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url_product(self):
            return reverse('products_by_category', args=[self.slug])
    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=200, default=None, blank=True)
    product_description = models.TextField(default=None,max_length=500, blank=True)
    product_ingridient = models.CharField(max_length=400, default=None, blank=True)
    product_highlights = models.TextField(default=None,max_length=500, blank=True)
    product_features = models.TextField(default=None,max_length=500, blank=True)
    product_image_1 = models.ImageField(upload_to='products', default = None)
    product_image_2 = models.ImageField(upload_to='products', default = None , blank = True)
    product_image_3 = models.ImageField(upload_to='products', default = None , blank = True)
    product_image_4 = models.ImageField(upload_to='products',blank = True)
    product_image_5 = models.ImageField(upload_to='products',blank = True)
    product_image_6 = models.ImageField(upload_to='products', blank = True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100,default=None)

    def get_url(self):
        return reverse('product_detail', args=[self.product_category.slug, self.slug])

    def __str__(self):
        return self.product_name
        
class ProductInformation(models.Model):
    spec_info = models.CharField(max_length=200, blank=True,default=None)
    specs = models.CharField(max_length=200, blank=True,default=None)
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
