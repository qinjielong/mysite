from django.contrib import admin
from .models import UserProfile, UserInfo

class UserProfileAdmin(admin.ModelAdmin): 
    list_display = ('user', 'birth', 'phone') 
    list_filter = ("phone",)

admin.site.register(UserProfile, UserProfileAdmin)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user", 'status', 'school', 'company', 'profession', 'employe_id', 'address', 'aboutme')
    list_filter = ("user", "company", "profession")

admin.site.register(UserInfo, UserInfoAdmin)
