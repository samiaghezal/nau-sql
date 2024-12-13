class StockCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.StockCountableEdge()
    totalCount = models.Int()

