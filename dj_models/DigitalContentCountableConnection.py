class DigitalContentCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.DigitalContentCountableEdge()
    totalCount = models.Int()

