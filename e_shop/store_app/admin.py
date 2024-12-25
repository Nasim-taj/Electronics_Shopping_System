from django.contrib import admin
from .models import *

# Register your models here.

class ImagesTublerinline(admin.TabularInline):
    model=Images

class TagsTublerinline(admin.TabularInline):
    model=Tag

class ProductAdmin(admin.ModelAdmin):
    inlines=[ImagesTublerinline,TagsTublerinline]

class OrderItemTubleinline(admin.TabularInline):
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemTubleinline]
    list_display = ['firstname','phone','email','date']
    search_fields = ['firstname','phone','email']


admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)
admin.site.register(Tag)
admin.site.register(Images)
admin.site.register(Contact_us)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
