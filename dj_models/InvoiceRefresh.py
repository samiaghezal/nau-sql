class InvoiceRefresh(models.Model):
    order = models.Order()
    nauticalOrder = models.NauticalOrder()
    invoiceErrors = models.InvoiceError()
    invoice = models.Invoice()

