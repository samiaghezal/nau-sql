class WishlistUpdate(models.Model):
    wishlistErrors = models.WishlistError()
    wishlist = models.Wishlist()

