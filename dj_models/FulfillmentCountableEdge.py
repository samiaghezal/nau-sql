class FulfillmentCountableEdge(models.Model):
    node = models.Fulfillment()
    cursor = models.String()

