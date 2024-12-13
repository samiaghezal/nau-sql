class AppCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.AppCountableEdge()
    totalCount = models.Int()

