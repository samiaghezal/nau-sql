class WishlistCountableEdge(models.Model):
    node = models.Wishlist()
    cursor = models.String()

