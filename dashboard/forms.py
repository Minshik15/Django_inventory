from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']
        labels = {
            'name': 'Нэр',
            'category': 'Ангилал',
            'quantity': 'Тоо ширхэг',
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','order_quantity']
        labels = {
            'product': 'бүтээгдэхүүн',
            'order_quantity': 'захиалгын_тоо',
        }