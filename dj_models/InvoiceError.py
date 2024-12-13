class InvoiceError(models.Model):
    field = models.String()
    message = models.String()
    code = models.InvoiceErrorCode()

