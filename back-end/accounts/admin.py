from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
# Register your models here.'

@admin.register(Account)
class AdminUser(UserAdmin):
    readonly_fields=["date_joined","last_login"]
    list_display_links=["email","username"]
    list_display=["email","username","first_name","last_name","phone_number","is_active","is_superuser","date_joined"]
    search_fields=["email","username"]
    ordering =["-date_joined"]
    filter_horizontal=[]
    list_filter=[]
    fieldsets = []
    add_fieldsets=[
        (
            None,{
            "classes":("wide"),
            "fields":('email',"username","first_name","last_name","phone_number","password1","password2")
        }
        ),
    ]
