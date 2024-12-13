class FontCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.FontCountableEdge()
    totalCount = models.Int()

