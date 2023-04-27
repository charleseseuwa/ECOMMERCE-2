from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category
from .models import Product
from .models import Subscriber
from .models import Social

# Create your views here.
def home_page(request):
    if request.method == "GET":

        all_categories = Category.objects.all()
        mens_products = Product.objects.filter(category=2)
        women_products = Product.objects.filter(category=1)
        kids_products = Product.objects.filter(category=3)
        social_products = Social.objects.all()
       
    elif request.method == "POST":
        new_subscribers_name = request.POST["name"] # Or request.POST.get(name)
        new_subscribers_email = request.POST.get("email") # Or request.POST["email"]

        Subscriber.objects.create(name=new_subscribers_name, email=new_subscribers_email)
        return redirect("home_page")  # this return the login to the home page
        # return HttpResponse("You have subscribed successfully")

    context = {

            "all_categories": all_categories,
            "mens_products": mens_products,
            "women_products": women_products,
            "kids_products": kids_products,
            "social_products": social_products    
        }

    return render(request, 'project/home.html', context)

def about_page(request):
    return render(request,'project/about.html' )

def contact_page(request):
    return render(request, 'project/contact.html')

def products_page(request):
    return render(request, 'prject/product.html')
