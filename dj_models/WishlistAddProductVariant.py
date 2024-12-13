class WishlistAddProductVariant(models.Model):
    wishlist = models.WishlistItem()
    wishlistErrors = models.WishlistError()

