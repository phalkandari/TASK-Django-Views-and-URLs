from django.shortcuts import HttpResponse, render
from django.http import HttpResponse


from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse("<h1> Welcome to this Products Website!!<h1/>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(
        f"""
                        <p>{product.id}</p>
                        <p>{product.name}</p>
                        <p>{product.price}</p>
                        """
    )
