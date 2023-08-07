from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddProductForm
from .models import Product


import socket
# Create your views here.

def home(request):
	
	products = Product.objects.all()
	data = {
		'products' : products, 
	}
	
	return render(request, 'product/home.html', data)

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

def product(request, id_product):

	product = get_object_or_404(Product, pk=id_product)
	return render(request, 'product/product.html', {'product' : product})

def delete(request, id_product):

	product = Product.objects.get(pk=id_product)
	product.delete()
	messages.success(request,"Đã xóa sản phẩm.")
	return redirect('home')

def add(request):
	form = AddProductForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			add = form.save()
			print(add)
			messages.success(request, "Product added successfully.")
			return redirect('home')
	else:
		return render(request, 'product/add.html', {'form':form})

def update(request, id_product):

	current_product = Product.objects.get(pk=id_product)
	form = AddProductForm(request.POST or None, request.FILES or None, instance=current_product)
	if form.is_valid():
		form.save()
		messages.success(request, "Cập nhật thành công")
		return redirect('home')
	return render(request, 'product/update.html', {'form':form})

def port(request, id_product):

	if request.method == "POST":
		product = Product.objects.get(pk=id_product)
		if request.POST['action'] == "Import":
			product.amount += int(request.POST['amount'])
			messages.success(request, "Import successfully")
		if request.POST['action'] == "Export":
			product.amount -= int(request.POST['amount'])
			messages.success(request, "Export successfully")
		product.save()
		return render(request, 'product/product.html', {'product' : product})
	else:
		messages.success(request, "Failed")
		return redirect('home')
