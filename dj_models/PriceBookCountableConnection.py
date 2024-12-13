class PriceBookCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PriceBookCountableEdge()
    totalCount = models.Int()

