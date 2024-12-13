class PriceBookVariantHistoryCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PriceBookVariantHistoryCountableEdge()
    totalCount = models.Int()

