from django.db import models
import PIL

# Create your models here.

class Product(models.Model):
	id_product = models.CharField(max_length=20, primary_key=True)
	title = models.CharField(max_length=100, null=False)
	img = models.ImageField(upload_to="Product/static/img", null=True)
	amount = models.IntegerField(default=0, null=False)
	price = models.DecimalField(max_digits=12, decimal_places=2)
	description = models.TextField(blank=True, null=True)
	company = models.CharField(max_length=50)

class History(models.Model):

	# id sinh tự động
	action = models.CharField(max_length=10, null=False) # Hành động người dùng
	id_product = models.CharField(max_length=20, null=False) # Sản phẩm bị tác động
	amount_on_action = models.IntegerField(default=0, null=False) # Số lượng sản phẩm bị tác động vd thêm 5 hay giảm 1
	amount_exists_on_time = models.IntegerField(default=0, null=False) # Số lượng sản phẩm tại thời gian hành động
	action_on_time = models.DateTimeField(auto_now_add=True) # Thời điểm hành động xảy ra
	user = models.CharField(max_length=50, null=False) # Người thực hiện
