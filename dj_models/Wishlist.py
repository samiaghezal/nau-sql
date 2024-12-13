class Wishlist(models.Model):
    id = models.ID()
    createdAt = models.DateTime()
    name = models.String()
    isDefault = models.Boolean()
    user = models.User()
    items = models.WishlistItemCountableConnection()

