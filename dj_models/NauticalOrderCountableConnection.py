class NauticalOrderCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.NauticalOrderCountableEdge()
    totalCount = models.Int()

