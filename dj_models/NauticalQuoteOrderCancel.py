class NauticalQuoteOrderCancel(models.Model):
    order = models.NauticalOrder()
    orderErrors = models.OrderError()

