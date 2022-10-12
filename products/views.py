from django.shortcuts import HttpResponse, render

# Create your views here.
def get_home(request):
    return HttpResponse("<h1> Welcome to this Drinks Website!!<h1/>")
