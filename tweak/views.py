from django.shortcuts import render,redirect,get_object_or_404
from product.models import *
from contact.models import Contact, Inquiry
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    category = Category.objects.all()
    product = Product.objects.raw('select * from product_product order by random() limit 6')
    context={
        'category':category,
        'product':product,
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def enquiry(request):
    if request.method == "POST":  #validation for contact form
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        inquiry = Inquiry(name=name,company_name=company_name,number=number,email=email,message=message)
        inquiry.save()
        messages.success(request, "we've got your Inquiry we will contact you soon")
        return redirect('home')
    return render(request,'gallery.html')

def contact(request):
    if request.method == "POST":  #validation for contact form
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(
            name=name,
            number=number,
            email=email,
            message=message)
        contact.save()
        messages.success(request, 'Thanks for contacting us your message has been send sucessfuly to Tweak')
        return redirect('home')
    return render(request,'contact.html')

def product(request, category_slug, product_slug):
    single_product = Product.objects.get(product_category__slug=category_slug, slug=product_slug)
    product_information = ProductInformation.objects.all()
    context = {
        'single_product': single_product,
        'product_information': product_information,
        }
    return render(request,'product-detail.html',context)

def shop(request,category_slug=None):
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(product_category=categories)
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().order_by('id')
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request,'shop.html',context)