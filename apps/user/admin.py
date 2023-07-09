from django.contrib import admin
from .models import Subscribe, Team


@admin.register(Subscribe)
class Admin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Team)
class Admin(admin.ModelAdmin):
    list_display = ['name']
