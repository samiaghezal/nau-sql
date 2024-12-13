class PriceBookProductTypeHistoryCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PriceBookProductTypeHistoryCountableEdge()
    totalCount = models.Int()

