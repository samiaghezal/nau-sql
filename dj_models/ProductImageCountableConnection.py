class ProductImageCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.ProductImageCountableEdge()
    totalCount = models.Int()

