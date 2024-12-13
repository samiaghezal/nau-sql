class SaleCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.SaleCountableEdge()
    totalCount = models.Int()

