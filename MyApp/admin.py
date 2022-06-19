from django.contrib import admin
from .models import Cars,Order,Customer,Contact
# Register your models here.

admin.site.register(Contact)
admin.site.register(Cars)
admin.site.register(Order)
admin.site.register(Customer)
