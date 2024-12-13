class InvoiceCancel(models.Model):
    invoiceErrors = models.InvoiceError()
    invoice = models.Invoice()

