class AttributeError(models.Model):
    field = models.String()
    message = models.String()
    code = models.ProductErrorCode()
    values = models.String()

