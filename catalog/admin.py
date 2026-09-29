from django.contrib import admin

from .models import Bin, Item


@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = ["label", "description"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "size_label", "condition", "bin"]
    list_filter = ["category", "condition", "bin"]
