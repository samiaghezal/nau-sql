class WishlistDelete(models.Model):
    wishlistErrors = models.WishlistError()
    wishlist = models.Wishlist()

