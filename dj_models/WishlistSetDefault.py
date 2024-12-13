class WishlistSetDefault(models.Model):
    wishlist = models.Wishlist()
    wishlistErrors = models.WishlistError()

