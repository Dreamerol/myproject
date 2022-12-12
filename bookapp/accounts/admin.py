from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


# Register your models here.

User_Model = get_user_model()

@admin.register(User_Model)
class BookUserAdmin(UserAdmin):
    pass
