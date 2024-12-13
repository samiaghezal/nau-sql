class WishlistItemCountableEdge(models.Model):
    node = models.WishlistItem()
    cursor = models.String()

