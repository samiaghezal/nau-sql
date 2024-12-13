class OrderEventCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.OrderEventCountableEdge()
    totalCount = models.Int()

