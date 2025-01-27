from django.contrib import admin
from .models import Level
# Register your models here.
@admin.register(Level)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , 'time']