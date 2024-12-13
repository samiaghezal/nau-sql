class InvoiceRequestDelete(models.Model):
    invoiceErrors = models.InvoiceError()
    invoice = models.Invoice()

