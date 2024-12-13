class InvoiceSendNotification(models.Model):
    invoiceErrors = models.InvoiceError()
    invoice = models.Invoice()

