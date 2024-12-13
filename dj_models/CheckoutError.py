class CheckoutError(models.Model):
    field = models.String()
    message = models.String()
    code = models.CheckoutErrorCode()
    variants = models.ID()

