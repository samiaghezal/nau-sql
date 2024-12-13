class VoucherCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.VoucherCountableEdge()
    totalCount = models.Int()

