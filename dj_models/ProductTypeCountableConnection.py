class ProductTypeCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.ProductTypeCountableEdge()
    totalCount = models.Int()

