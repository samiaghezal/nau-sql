class InvoiceDelete(models.Model):
    invoiceErrors = models.InvoiceError()
    invoice = models.Invoice()
