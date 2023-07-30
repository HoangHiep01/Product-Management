from django.db import models
import PIL

# Create your models here.

class Product(models.Model):
	id_product = models.CharField(max_length=20, primary_key=True)
	title = models.CharField(max_length=100, null=False)
	img = models.ImageField(upload_to="static/product/", null=True)
	amount = models.IntegerField(default=0, null=False)
	price = models.DecimalField(max_digits=12, decimal_places=2)
	description = models.TextField(blank=True, null=True)
	company = models.CharField(max_length=50)