from django.contrib import admin
from .models import Subscribe


@admin.register(Subscribe)
class Admin(admin.ModelAdmin):
    list_display = ['email']
