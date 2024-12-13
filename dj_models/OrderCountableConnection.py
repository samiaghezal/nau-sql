class OrderCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.OrderCountableEdge()
    totalCount = models.Int()

