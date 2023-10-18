from django.contrib import admin
from .models import Category, Property

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['type']


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['category','price','image']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Property, PropertyAdmin)