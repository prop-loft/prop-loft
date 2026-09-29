from django.shortcuts import render

from .models import Item


def item_list(request):
    items = Item.objects.select_related("bin")
    return render(request, "catalog/item_list.html", {"items": items})
