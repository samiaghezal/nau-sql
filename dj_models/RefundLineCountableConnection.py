class RefundLineCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.RefundLineCountableEdge()
    totalCount = models.Int()

