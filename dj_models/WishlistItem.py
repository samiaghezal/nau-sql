class WishlistItem(models.Model):
    id = models.ID()
    wishlist = models.Wishlist()
    product = models.Product()
    variant = models.ProductVariant()
    note = models.String()
    expiryDate = models.DateTime()
    quantity = models.Int()
    requestedPrice = models.Money()

