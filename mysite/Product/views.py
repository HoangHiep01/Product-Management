from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product


import socket
# Create your views here.

def home(request):
	# if request.method == 'POST':
	# 	login_user(request)
	
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
	if request.method == 'POST':
		context['ID_auto'] = request.POST['postData']
	return render(request, 'product/scan.html', context) 

# def take_ID(request):

# 	print("Take: ", request.method)
# 	if request.method == 'POST':
# 		print("Take if: ", request.POST['id_product'])
# 		id_product = request.POST['id_product']
# 		detail(request, id_product)
# 	else:
# 		return redirect('scan') 

def detail(request):
	
	print("Detail: ", request.method)
	if request.method == 'POST':
		print("Detail if: ", request.POST['id_product'])
		id_product = request.POST['id_product']
		product = get_object_or_404(Product, pk=id_product)
		
		# product.img = product.img[15:]
		# print(product.img)

	return render(request, 'product/detail.html', {'product' : product})

def detail2(request, id_product):

	product = get_object_or_404(Product, pk=id_product)
	return render(request, 'product/detail.html', {'product' : product})
