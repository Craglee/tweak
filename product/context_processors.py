from . models import Category, Product

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def product_link(request):
    products_link = Product.objects.raw('select * from product_product order by random()')
    return dict(products_link=products_link)