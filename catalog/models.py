from django.db import models


class Bin(models.Model):
    """A labeled storage bin in the loft. Every item lives in exactly one."""

    label = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["label"]

    def __str__(self):
        return self.label


class Item(models.Model):
    """Anything a production stores and lends out: costumes in version 1."""

    class Category(models.TextChoices):
        COSTUME = "costume", "Costume"
        PROP = "prop", "Prop"
        SET_PIECE = "set_piece", "Set piece"

    class Condition(models.IntegerChoices):
        POOR = 1, "Poor"
        WORN = 2, "Worn"
        GOOD = 3, "Good"
        VERY_GOOD = 4, "Very good"
        NEW = 5, "Like new"

    name = models.CharField(max_length=120, db_index=True)
    category = models.CharField(max_length=20, choices=Category, default=Category.COSTUME)
    size_label = models.CharField(max_length=20, blank=True)
    condition = models.PositiveSmallIntegerField(choices=Condition, default=Condition.GOOD)
    # PROTECT: emptying a bin must not silently delete what was in it.
    bin = models.ForeignKey(Bin, on_delete=models.PROTECT, related_name="items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
