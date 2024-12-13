class PageCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PageCountableEdge()
    totalCount = models.Int()

