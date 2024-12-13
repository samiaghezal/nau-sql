class MediaCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.MediaCountableEdge()
    totalCount = models.Int()

