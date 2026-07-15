from django.contrib import admin
from .models import Adminporduct

@admin.register(Adminporduct)
class AdminProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'price', 'dec']