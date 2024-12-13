class PriceBookError(models.Model):
    field = models.String()
    message = models.String()
    code = models.PriceBookErrorCode()

