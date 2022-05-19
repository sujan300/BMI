
  
from django.contrib import admin
from account.models import Account,OtpEmail
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display        = ['id','first_name','last_name','age','email','joined_date','last_login','is_active','is_admin','is_superuser']
    list_display_links  = ['first_name','email']
    ordering = ('-joined_date',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)




class OtpEmailAdmin(admin.ModelAdmin):
    list_display = ["id","otp","user"]

admin.site.register(OtpEmail,OtpEmailAdmin)