from django import forms 
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all_'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all_'
        

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all_'
        
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all_'
        
        
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all_'
        

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = '__all_'
        
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all_'
        
        
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all_'
        
        
class NotificationForm(forms.ModelForm):
    class Meta:
        model =Notification
        fields = '__all_'
