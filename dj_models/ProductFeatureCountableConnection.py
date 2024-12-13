class ProductFeatureCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.ProductFeatureCountableEdge()
    totalCount = models.Int()

