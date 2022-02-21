from django.contrib import admin
from . models import Contact, Inquiry
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','number')

admin.site.register(Contact,ContactAdmin)

class InquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','number','company_name')

admin.site.register(Inquiry,InquiryAdmin)