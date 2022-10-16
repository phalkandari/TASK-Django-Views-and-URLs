from django.shortcuts import HttpResponse, render
from django.http import HttpResponse
from django.http import Http404


from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse("<h1> Welcome to this Products Website!!<h1/>")


def get_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404
    return render(request, "product_detail.html", {"product": product})


def get_products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


# You create a loop if you want to filter the items inside the list
