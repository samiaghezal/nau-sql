class VariantFeatureCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.VariantFeatureCountableEdge()
    totalCount = models.Int()

