class DraftOrderSetTransactionCurrency(models.Model):
    order = models.Order()
    orderErrors = models.OrderError()

