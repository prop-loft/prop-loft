# Modified to route item-detail requests.
from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("items/<int:pk>/", views.item_detail, name="item_detail"),
]
