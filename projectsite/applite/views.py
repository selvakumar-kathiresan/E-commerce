from django.shortcuts import render,redirect
from applite.models import *
from django.contrib import messages
from applite.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout

def home(request):
	products=Product.objects.filter(trending=1)
	return render(request,'apps/index.html',{"products":products})

def logout_page(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request,"Logged out Successfully")
	return redirect('/Home')

def login_page(request):
	if request.user.is_authenticated:
		return redirect('/Home')
	else:
		if request.method=='POST':
			name=request.POST.get('username')
			pwd=request.POST.get('password')
			user=authenticate(request,username=name,password=pwd)
			if user is not None:
				login(request,user)
				messages.success(request,"Successfully Logged in")
				return redirect('/Home')
			else:
				messages.success(request,"Invalid Username or Password")
				return register('/login')
		return render(request,'apps/login.html')

def register(request):
	form=CustomUserForm()
	if request.method=='POST':
		form=CustomUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login')
			messages.success(request,"Registration success You can login Now...!")
	return render(request,'apps/register.html',{"form":form})

def collections(request):
	catagory=Catagory.objects.filter(status=0)
	return render(request,'apps/collections.html',{"catagory":catagory})

def collectionview(request,name):
	if(Catagory.objects.filter(name=name,status=0)):
		products=Product.objects.filter(catagory__name=name)
		return render(request,'product/index.html',{"products":products,"catagory_name":name})
	else:
		messages.warning(request,"No such Catagory Found")
		return redirect('/collections')

def product_details(request,cname,pname):
	if(Catagory.objects.filter(name=cname,status=0)):
		if(Product.objects.filter(name=pname,status=0)):
			products=Product.objects.filter(name=pname,status=0).first()
			return render(request,'product/product_details.html',{"products":products})		
		else:
			messages.error(request,"No such Product Found")
			return redirect('/collections')
	else:
		messages.error(request,"No such Catagory Found")
		return redirect('/collections')
	
	
