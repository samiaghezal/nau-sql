class WishlistAddProduct(models.Model):
    wishlist = models.WishlistItem()
    wishlistErrors = models.WishlistError()

