class ProductCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.ProductCountableEdge()
    totalCount = models.Int()

