class PriceBookProductCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PriceBookProductCountableEdge()
    totalCount = models.Int()

