class ExportFileCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.ExportFileCountableEdge()
    totalCount = models.Int()

