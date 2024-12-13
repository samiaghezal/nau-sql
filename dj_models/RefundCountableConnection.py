class RefundCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.RefundCountableEdge()
    totalCount = models.Int()

