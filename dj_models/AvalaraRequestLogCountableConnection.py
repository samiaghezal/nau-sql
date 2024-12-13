class AvalaraRequestLogCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.AvalaraRequestLogCountableEdge()
    totalCount = models.Int()

