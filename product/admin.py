from django.contrib import admin
from . models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_category','slug')
    prepopulated_fields = {'slug' : ('product_name',)}
admin.site.register(Product,ProductAdmin)

class ProductInformationAdmin(admin.ModelAdmin):
    list_display = ('product','spec_info','specs')
admin.site.register(ProductInformation,ProductInformationAdmin)
