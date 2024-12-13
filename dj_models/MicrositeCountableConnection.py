class MicrositeCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.MicrositeCountableEdge()
    totalCount = models.Int()

