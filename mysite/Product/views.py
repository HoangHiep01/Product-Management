from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddProductForm
from .models import Product, History
import functools


# import socket
# Create your views here.

def save_history(request, action='undefined', id_product='undefined', amount_on_action=0, amount_exists_on_time=0):
	history = History.objects.all()
	history.create(action=action, id_product=id_product, amount_on_action=amount_on_action, amount_exists_on_time=amount_exists_on_time, user=request.user)

def home(request):
	
	if request.method == "POST":
		login_user(request)

	if request.user.is_authenticated:
		products = Product.objects.all()
		data = {
			'products' : products, 
		}
		return render(request, 'product/home.html', data)
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

def auth_decorator(func):

	@functools.wraps(func)
	def warpper(*args, **kwargs):
		request = args[0]
		if request.user.is_authenticated:
			result = func(*args, **kwargs)
			return result
		else:
			print("Decorator is working.")
			messages.warning(request, "Bạn cần đăng nhập để thực hiện chức năng")
			return redirect('home')
	return warpper

@auth_decorator
def delete(request, id_product):
	product = Product.objects.get(pk=id_product)
	product.delete()
	save_history(request=request, action="DELETE", id_product=id_product, amount_on_action=product.amount, amount_exists_on_time=product.amount)
	messages.success(request,"Đã xóa sản phẩm.")
	return redirect('home')

@auth_decorator
def add(request):

	form = AddProductForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			add = form.save()
			save_history(request=request, action="ADD", id_product=request.POST['id_product'], amount_on_action=request.POST['amount'])
			messages.success(request, "Thêm sản phẩm thành công")
			return redirect('home')
	else:
		return render(request, 'product/add.html', {'form':form})

@auth_decorator
def update(request, id_product):

	current_product = Product.objects.get(pk=id_product)
	form = AddProductForm(request.POST or None, request.FILES or None, instance=current_product)
	if form.is_valid():
		form.save()
		save_history(request=request, action="UPDATE", id_product=id_product)
		messages.success(request, "Cập nhật thành công")
		return redirect('home')
	return render(request, 'product/update.html', {'form':form})

@auth_decorator
def port(request, id_product):

	if request.method == "POST":
		product = Product.objects.get(pk=id_product)
		if request.POST['action'] == "Import":
			save_history(request=request, action="IMPORT", id_product=id_product, amount_on_action=int(request.POST['amount']), amount_exists_on_time=product.amount)
			product.amount += int(request.POST['amount'])
			messages.success(request, "Nhập thành công.")
		if request.POST['action'] == "Export":
			save_history(request=request, action="EXPORT", id_product=id_product, amount_on_action=int(request.POST['amount']), amount_exists_on_time=product.amount)
			product.amount -= int(request.POST['amount'])
			messages.success(request, "Xuất thành công.")
		product.save()
		return render(request, 'product/product.html', {'product' : product})
	else:
		messages.success(request, "Failed")
		return redirect('home')
			
@auth_decorator
def history(request):

	historys = History.objects.all()
	data = {
		'historys' : historys
	}
	return render(request, 'product/history.html', data)