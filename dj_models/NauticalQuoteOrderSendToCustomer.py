class NauticalQuoteOrderSendToCustomer(models.Model):
    order = models.NauticalOrder()
    orderErrors = models.OrderError()

