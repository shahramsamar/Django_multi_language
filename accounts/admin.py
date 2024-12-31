from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile
# 1 from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms



class CustomUserAdmin(UserAdmin):
    model = User
    # 1 add_form = CustomUserCreationForm
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    searching_fields =('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentications', {
            "fields": ('email', 'password'
                
            ),
        }),
        
        ('permissions', {
            "fields": ('is_staff', 'is_active', 'is_superuser'
                
            ),
        }),
        
        ('group permissions', {
            "fields": ('groups', 'user_permissions'
                
            ),
        }),
        
        ('important date', {
            "fields": ('last_login',
                
            ),
        }),
        
        
    )
    add_fieldsets =(
        ( None,{
            'classes':('wide',),
            'fields':('email', 'password1', 'password2' , 'is_staff', 'is_active', 'is_superuser')
        }
            
        ),
        
    )
    
admin.site.register(Profile)    
admin.site.register(User, CustomUserAdmin)    