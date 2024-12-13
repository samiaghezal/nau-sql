class ContentCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.ContentCountableEdge()
    totalCount = models.Int()

