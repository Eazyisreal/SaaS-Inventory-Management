from django.contrib import admin
from .models import *
from .forms import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff']
    form = UserForm
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'quantity']
    form = ProductForm
    list_filter = ['category']
    search_fields = ['category', 'name']
    
class SupplierAdmin(admin.ModelAdmin):
    list_display = '__all__'
    form = ProductForm
    list_filter = ['name']
    search_fields = ['email', 'name']

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Notification)



