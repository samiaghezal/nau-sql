class SellerCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.SellerCountableEdge()
    totalCount = models.Int()

