from django.contrib import admin

# Register your models here.


from.models import Product,cart,checkout,Order


admin.site.register(Product)
admin.site.register(cart)
admin.site.register(Order)
admin.site.register(checkout)
 
 
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'host', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')


 
 
    