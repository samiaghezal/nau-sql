class GroupCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.GroupCountableEdge()
    totalCount = models.Int()

