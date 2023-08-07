from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.home, name='home'),
	path('login', views.login_user, name='login'),
	path('logout', views.logout_user, name='logout'),
	path('scan', views.scan_ID, name='scan'),
	# path('take/', views.take_ID, name='take'),
	path('detail', views.detail, name='detail'),
	path('product/<str:id_product>', views.product, name='product'),
	path('add', views.add, name='add'),
	path('delete/<str:id_product>', views.delete, name='delete'),
	path('update/<str:id_product>', views.update, name='update'),
	path('port/<str:id_product>', views.port, name='port'),
]