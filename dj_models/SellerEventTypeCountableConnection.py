class SellerEventTypeCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.SellerEventTypeCountableEdge()
    totalCount = models.Int()

