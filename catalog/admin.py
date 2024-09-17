from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )