class WishlistCreate(models.Model):
    wishlistErrors = models.WishlistError()
    wishlist = models.Wishlist()

