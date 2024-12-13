class ProductVariantCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.ProductVariantCountableEdge()
    totalCount = models.Int()

