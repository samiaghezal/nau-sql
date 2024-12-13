class SellerError(models.Model):
    field = models.String()
    message = models.String()
    code = models.SellerErrorCode()

