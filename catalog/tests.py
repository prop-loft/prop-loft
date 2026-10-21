# Modified to cover item-detail fields, navigation, and missing items.
from django.test import TestCase
from django.urls import reverse

from .models import Bin, Item


class ItemListTests(TestCase):
    def test_lists_every_item_with_its_bin(self):
        bin_a = Bin.objects.create(label="A-01")
        waistcoat = Item.objects.create(name="Victorian waistcoat", size_label="M", bin=bin_a)
        hat = Item.objects.create(name="Bowler hat", bin=bin_a)

        response = self.client.get(reverse("catalog:item_list"))

        self.assertContains(response, "Victorian waistcoat")
        self.assertContains(response, "Bowler hat")
        self.assertContains(response, "A-01")
        for item in (waistcoat, hat):
            self.assertContains(
                response,
                f'<a href="{reverse("catalog:item_detail", args=[item.pk])}">{item.name}</a>',
                html=True,
            )

    def test_says_so_when_the_catalog_is_empty(self):
        response = self.client.get(reverse("catalog:item_list"))

        self.assertContains(response, "Nothing in the catalog yet")


class ItemDetailTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        bin_a = Bin.objects.create(label="A-01")
        cls.item = Item.objects.create(
            name="Victorian waistcoat",
            category=Item.Category.COSTUME,
            size_label="M",
            condition=Item.Condition.VERY_GOOD,
            bin=bin_a,
        )

    def test_shows_the_item_fields_and_a_link_back_to_the_catalog(self):
        url = reverse("catalog:item_detail", args=[self.item.pk])
        self.assertEqual(url, f"/items/{self.item.pk}/")

        response = self.client.get(url)

        self.assertTemplateUsed(response, "catalog/item_detail.html")
        for field in ("Victorian waistcoat", "Costume", "M", "Very good", "A-01"):
            self.assertContains(response, f"<dd>{field}</dd>", html=True)
        self.assertContains(
            response,
            f'<a href="{reverse("catalog:item_list")}">Back to catalog</a>',
            html=True,
        )

    def test_missing_item_returns_404(self):
        response = self.client.get(reverse("catalog:item_detail", args=[self.item.pk + 1]))

        self.assertEqual(response.status_code, 404)

    def test_empty_size_uses_the_catalog_placeholder(self):
        self.item.size_label = ""
        self.item.save()

        response = self.client.get(reverse("catalog:item_detail", args=[self.item.pk]))

        self.assertContains(response, "<dd>—</dd>", html=True)
