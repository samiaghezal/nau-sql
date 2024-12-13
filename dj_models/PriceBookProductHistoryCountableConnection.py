class PriceBookProductHistoryCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PriceBookProductHistoryCountableEdge()
    totalCount = models.Int()

