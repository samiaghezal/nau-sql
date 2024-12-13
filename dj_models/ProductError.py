class ProductError(models.Model):
    field = models.String()
    message = models.String()
    code = models.ProductErrorCode()
    attributes = models.ID()

