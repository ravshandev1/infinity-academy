from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class Admin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['is_read']
