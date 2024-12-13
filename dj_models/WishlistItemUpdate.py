class WishlistItemUpdate(models.Model):
    wishlistErrors = models.WishlistError()
    wishlistItem = models.WishlistItem()

