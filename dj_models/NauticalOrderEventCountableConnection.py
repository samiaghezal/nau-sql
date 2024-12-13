class NauticalOrderEventCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.NauticalOrderEventCountableEdge()
    totalCount = models.Int()

