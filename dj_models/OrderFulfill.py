class OrderFulfill(models.Model):
    fulfillments = models.Fulfillment()
    order = models.Order()
    orderErrors = models.OrderError()

