from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):

	id_product = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Mã sản phẩm", "class":"form-control"}), label="")
	title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tên sản phẩm", "class":"form-control"}), label="")
	img = forms.ImageField()
	amount = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Só lượng sản phẩm", "class":"form-control"}), label="")
	price = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Giá sản phẩm", "class":"form-control"}), label="")
	description = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"Mô tả sản phẩm", "class":"form-control"}), label="")
	company = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Tên công ty", "class":"form-control"}), label="")

	class Meta():
		model = Product
		exclude = ("user","",)