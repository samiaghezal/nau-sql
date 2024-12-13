class NauticalDraftOrderSetTransactionCurrency(models.Model):
    nauticalOrder = models.NauticalOrder()
    orderErrors = models.OrderError()

