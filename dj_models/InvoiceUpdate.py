class InvoiceUpdate(models.Model):
    invoiceErrors = models.InvoiceError()
    invoice = models.Invoice()

