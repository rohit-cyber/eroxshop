from django.shortcuts import render
from django.views import View
from .models import Product,Customer,Cart,OrderPlaced

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwear=Product.objects.filter(category='TW')
        bottomwear=Product.objects.filter(category='BW')
        mobile=Product.objects.filter(category='M')
        dictt={'topwear':topwear,'bottomwear':bottomwear,'mobile':mobile}
        return render(request,'app/home.html',context=dictt)


class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(id=pk)
        return render(request,'app/productdetail.html',{'product':product})

def mobile(request,data=None):
    if data == None:
        product=Product.objects.filter(category='M')
    elif data=='Samsung':
        product=Product.objects.filter(category='M').filter(brand='samsung')
    elif data=='Apple':
        product=Product.objects.filter(category='M').filter(brand='apple')
    elif data=='Above':
        product=Product.objects.filter(category='M').filter(discounted_price__gt=500)
    elif data=='Below':
        product=Product.objects.filter(category='M').filter(discounted_price__lt=500)
    return render(request, 'app/mobile.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')



def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
