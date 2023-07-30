from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.home, name='home'),
	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('scan/', views.scan_ID, name='scan'),
	# path('take/', views.take_ID, name='take'),
	path('detail/', views.detail, name='detail'),
	path('detail2/<str:id_product>', views.detail2, name='detail2'),
]