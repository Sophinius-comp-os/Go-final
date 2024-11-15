from django.contrib import admin
from myapp.models import Member
from myapp.models import Product
from myapp.models import Appointment
from myapp.models import Contact


# Register your models here.
admin.site.register(Member)
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Contact)


