from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .models import Product,Customer,Cart,OrderPlaced
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from .forms import CustomerForm

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


class CustomerRegistration(View):
    def get(self,request):
        return render(request, 'app/customerregistration.html')
    
    def post(self,request):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.error(request,'email already exists')
                return redirect('customerregistration')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,'you have successfully registered')
                return redirect('login')
        else:
            messages.error(request,'Password did not match')
            return redirect('customerregistration')

class Login(View):
    def get(self,request):
        return render(request,'app/login.html',)
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('product')
        else:
            return HttpResponse('Invalid Credentials')

def logout(request):
    auth.logout(request)
    return redirect('product')


class CustomerProfile(View):
    def get(self,request):
        form=CustomerForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form=CustomerForm(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
        return redirect('product')



 

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







def checkout(request):
 return render(request, 'app/checkout.html')
