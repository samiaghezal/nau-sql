class PriceBookProductTypeCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PriceBookProductTypeCountableEdge()
    totalCount = models.Int()

