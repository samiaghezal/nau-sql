class NauticalDraftOrderComplete(models.Model):
    order = models.NauticalOrder()
    sellerOrders = models.Order()
    orderErrors = models.OrderError()

