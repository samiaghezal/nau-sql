class CollectionCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.CollectionCountableEdge()
    totalCount = models.Int()

