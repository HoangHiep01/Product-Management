from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddProductForm
from .models import Product, History


# import socket
# Create your views here.

def save_history(action='undefined', id_product='undefined', amount_on_action=0, amount_exists_on_time=0, user='undefined'):
	history = History.objects.all()
	history.create(action=action, id_product=id_product, amount_on_action=amount_on_action, amount_exists_on_time=amount_exists_on_time, user=user)

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
		messages.error(request, f"Không tìm thấy tài khoản.")
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
	
	# print("Detail: ", request.method)
	if request.method == 'POST':
		# print("Detail if: ", request.POST['id_product'])
		id_product = request.POST['id_product']
		# product = get_object_or_404(Product, pk=id_product)
		list_product = Product.objects.filter(pk=id_product)
		if list_product.exists():
			product = Product.objects.get(pk=id_product)
			# # product.img = product.img.replace('Product/','')
			# print(product.img, type(product.img))
			return render(request, 'product/detail.html', {'product' : product})
		else:
			messages.warning(request, f"Không tìm thấy sản phẩm có mã {id_product}. Bạn có thể sản phẩm mới.")
			# return render(request, 'product/scan.html', {'ID_auto' : f'{id_product}'})
			return redirect('scan')

	return redirect('home')


def product(request, id_product):

	product = get_object_or_404(Product, pk=id_product)
	return render(request, 'product/product.html', {'product' : product})

def delete(request, id_product):

	product = Product.objects.get(pk=id_product)
	product.delete()
	save_history(action="DELETE", id_product=id_product, amount_on_action=product.amount, amount_exists_on_time=product.amount)
	messages.success(request,"Đã xóa sản phẩm.")
	return redirect('home')

def add(request):
	form = AddProductForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			add = form.save()
			save_history(action="ADD", id_product=request.POST['id_product'], amount_on_action=request.POST['amount'])
			messages.success(request, "Thêm sản phẩm thành công")
			return redirect('home')
	else:
		return render(request, 'product/add.html', {'form':form})

def update(request, id_product):

	current_product = Product.objects.get(pk=id_product)
	form = AddProductForm(request.POST or None, request.FILES or None, instance=current_product)
	if form.is_valid():
		form.save()
		save_history(action="UPDATE", id_product=id_product)
		messages.success(request, "Cập nhật thành công")
		return redirect('home')
	return render(request, 'product/update.html', {'form':form})

def port(request, id_product):

	if request.method == "POST":
		product = Product.objects.get(pk=id_product)
		if request.POST['action'] == "Import":
			save_history(action="IMPORT", id_product=id_product, amount_on_action=int(request.POST['amount']), amount_exists_on_time=product.amount)
			product.amount += int(request.POST['amount'])
			messages.success(request, "Nhập thành công.")
		if request.POST['action'] == "Export":
			save_history(action="EXPORT", id_product=id_product, amount_on_action=int(request.POST['amount']), amount_exists_on_time=product.amount)
			product.amount -= int(request.POST['amount'])
			messages.success(request, "Xuất thành công.")
		product.save()
		return render(request, 'product/product.html', {'product' : product})
	else:
		messages.success(request, "Failed")
		return redirect('home')

def history(request):
	historys = History.objects.all()
	data = {
		'historys' : historys
	}
	return render(request, 'product/history.html', data)