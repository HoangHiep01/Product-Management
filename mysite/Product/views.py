from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Product


import socket
# Create your views here.

def home(request):
	if request.method == 'POST':
		login_user(request)
	
	return render(request, 'product/home.html', {})

def login_user(request):

	print(request.method)
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		# messages.success(request, "Đăng nhập thành công.")
		return redirect('home')
	else:
		print("Failed")
		messages.success(request, f"Không tìm thấy tài khoản.")
		return redirect('home')

def logout_user(request):
	logout(request)
	messages.success(request, "Bạn đã đăng xuất.")
	return redirect('home')

def scan_ID(request):

	context = {
		'ID_auto' : 'ID0000'
	}
	return render(request, 'product/scan.html', context) 

def detail(request):
	
	print("Detail: ", request.method)
	if request.method == 'POST':
		print("Detail if: ", request.POST['id_product'])
		id_product = request.POST['id_product']
		product = get_object_or_404(Product, pk=id_product)
		
		# product.img = product.img[15:]
		# print(product.img)

	return render(request, 'product/detail.html', {'product' : product})

def product(request, id_product):

	product = get_object_or_404(Product, pk=id_product)
	return render(request, 'product/product.html', {'product' : product})

def register_user(request):
	
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Đăng ký thành công!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'product/register.html', {'form':form})