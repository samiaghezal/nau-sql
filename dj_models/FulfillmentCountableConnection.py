class FulfillmentCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.FulfillmentCountableEdge()
    totalCount = models.Int()

