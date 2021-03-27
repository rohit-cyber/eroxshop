from django.contrib import admin
from .models import Customer,Product,OrderPlaced,Cart

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','description','brand','category','product_image']

class CartAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity']

class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['user','customer','product','quantity','ordered_date','status']

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(OrderPlaced,OrderPlacedAdmin)


