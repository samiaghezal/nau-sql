class PriceBookVariantCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PriceBookVariantCountableEdge()
    totalCount = models.Int()

