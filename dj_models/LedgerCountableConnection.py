class LedgerCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.LedgerCountableEdge()
    totalCount = models.Int()

