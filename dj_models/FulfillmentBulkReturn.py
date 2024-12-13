class FulfillmentBulkReturn(models.Model):
    fulfillments = models.Fulfillment()
    orderErrors = models.OrderError()

