from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10
    search_fields = ['title']

class RecipeItemInline(admin.TabularInline):
    autocomplete_fields = ['ingredient']
    min_num = 1
    max_num = 10
    model = models.RecipeItem
    extra = 0

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeItemInline]
