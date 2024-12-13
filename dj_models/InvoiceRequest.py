class InvoiceRequest(models.Model):
    order = models.Order()
    nauticalOrder = models.NauticalOrder()
    refund = models.Refund()
    invoiceErrors = models.InvoiceError()
    invoice = models.Invoice()

