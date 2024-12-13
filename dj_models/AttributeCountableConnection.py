class AttributeCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.AttributeCountableEdge()
    totalCount = models.Int()

