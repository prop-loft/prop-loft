from django.test import TestCase
from django.urls import reverse

from .models import Bin, Item


class ItemListTests(TestCase):
    def test_lists_every_item_with_its_bin(self):
        bin_a = Bin.objects.create(label="A-01")
        Item.objects.create(name="Victorian waistcoat", size_label="M", bin=bin_a)
        Item.objects.create(name="Bowler hat", bin=bin_a)

        response = self.client.get(reverse("catalog:item_list"))

        self.assertContains(response, "Victorian waistcoat")
        self.assertContains(response, "Bowler hat")
        self.assertContains(response, "A-01")

    def test_says_so_when_the_catalog_is_empty(self):
        response = self.client.get(reverse("catalog:item_list"))

        self.assertContains(response, "Nothing in the catalog yet")
