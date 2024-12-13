class PaymentError(models.Model):
    field = models.String()
    message = models.String()
    code = models.PaymentErrorCode()

