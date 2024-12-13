class WishlistCreateForBuyer(models.Model):
    wishlistErrors = models.WishlistError()
    wishlist = models.Wishlist()

