class PayoutError(models.Model):
    field = models.String()
    message = models.String()
    code = models.PayoutErrorCode()

