from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserForm

class CustomUserAdmin(UserAdmin):
   UserAdmin.list_display += ('is_dboy','city','formsubmitted','vacinated','merit') 
   UserAdmin.list_filter += ('is_dboy','city','formsubmitted','vacinated','merit')
   UserAdmin.fieldsets += (('is_dboy', {'fields': ('is_dboy','city','formsubmitted','vacinated','merit')}),) 
  
  


admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register(Orderer)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)