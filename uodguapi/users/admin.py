from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Guild, CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff']

admin.site.register(Guild)
admin.site.register(CustomUser, CustomUserAdmin)
