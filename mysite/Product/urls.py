from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.home, name='home'),
	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('scan', views.scan_ID, name='scan'),
	path('detail', views.detail, name='detail'),
	path('product/<str:id_product>', views.product, name='product'),
	path('register', views.register_user, name='register'),
]