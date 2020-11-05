from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import MyUser,Profile,Item,OrderItem,Order,Address,Coupon
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title','price','slug','img']
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user','item','quantity','ordered']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','start_date','order_date','Ordered']
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','country','city','street_address']
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','amount']
admin.site.register(MyUser,UserAdmin)
admin.site.register(Profile)
admin.site.register(Item,ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order,OrderAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Coupon,CouponAdmin)

