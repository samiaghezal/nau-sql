class WishlistRemoveProductVariant(models.Model):
    wishlist = models.WishlistItem()
    wishlistErrors = models.WishlistError()

