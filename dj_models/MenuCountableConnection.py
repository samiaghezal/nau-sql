class MenuCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.MenuCountableEdge()
    totalCount = models.Int()

