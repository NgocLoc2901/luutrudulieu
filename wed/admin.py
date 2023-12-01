from django.contrib import admin
from .models import *
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Oder)
admin.site.register(OderItem)
admin.site.register(ShippingAddress)
# Register your models here.
