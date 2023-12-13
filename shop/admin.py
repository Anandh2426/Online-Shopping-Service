from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description')


admin.site.register(Catagory,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
