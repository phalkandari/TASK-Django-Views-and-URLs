from django.shortcuts import HttpResponse, render
from django.http import HttpResponse


from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse("<h1> Welcome to this Products Website!!<h1/>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, "product_detail.html", context)


def get_products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


# You create a loop if you want to filter the items inside the list
