class PayoutCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PayoutCountableEdge()
    totalCount = models.Int()

