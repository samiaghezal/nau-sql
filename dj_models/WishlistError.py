class WishlistError(models.Model):
    field = models.String()
    message = models.String()
    code = models.WishlistErrorCode()

