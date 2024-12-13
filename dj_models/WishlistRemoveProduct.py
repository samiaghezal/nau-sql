class WishlistRemoveProduct(models.Model):
    wishlist = models.WishlistItem()
    wishlistErrors = models.WishlistError()

