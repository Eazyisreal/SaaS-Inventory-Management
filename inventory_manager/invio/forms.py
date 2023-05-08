from django import forms 
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

        # Add crispy form classes to the form fields
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4 control-label'
        self.helper.field_class = 'col-md-8'
        

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
        
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
        

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = '__all__'
        
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
        
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        
        
class NotificationForm(forms.ModelForm):
    class Meta:
        model =Notification
        fields = '__all__'
