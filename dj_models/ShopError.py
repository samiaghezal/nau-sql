class ShopError(models.Model):
    field = models.String()
    message = models.String()
    code = models.ShopErrorCode()

