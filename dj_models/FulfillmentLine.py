class FulfillmentLine(models.Model):
    id = models.ID()
    quantity = models.Int()
    orderLine = models.OrderLine()
    returnReason = models.String()

