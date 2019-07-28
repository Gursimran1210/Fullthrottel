from django.shortcuts import render
from .models import Product,Contact

# Create your views here.
def index(request):
    product = Product.objects
    return render(request,'shop/shop.html',{'product': product})

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('name','')
        lname = request.POST.get('lname','')
        email = request.POST.get('email','')
        comment = request.POST.get('comment','')
        contact = Contact(first_name=first_name,last_name=lname,email=email,comment=comment)
        contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def productview(request):
    products = Product.objects
    return render(request,'shop/productview.html',{'products':products})

def checkout(request):
    return render(request,'shop/checkout.html')

def new(request):
    return render(request,'shop/New.html')




