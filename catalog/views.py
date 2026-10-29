# Modified to expose an item's details beside the existing catalog list.
from django.shortcuts import get_object_or_404, render

from .models import Item


def item_list(request):
    items = Item.objects.select_related("bin")
    return render(request, "catalog/item_list.html", {"items": items})


def item_detail(request, pk):
    item = get_object_or_404(Item.objects.select_related("bin"), pk=pk)
    return render(request, "catalog/item_detail.html", {"item": item})
