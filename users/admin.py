from django.contrib import admin

from users.models import User


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'password', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')



