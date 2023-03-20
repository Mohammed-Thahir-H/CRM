from django.contrib import admin

# Register your models here.
from .models import Register

# class RegisterAdmin(admin.ModelAdmin):
#     list_display=("Firstname","Lastname","Email","PhoneNo","Password")

admin.site.register(Register)