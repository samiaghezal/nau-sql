class FulfillmentReturnStatusBulkUpdate(models.Model):
    fulfillment = models.Fulfillment()
    order = models.Order()
    orderErrors = models.OrderError()

