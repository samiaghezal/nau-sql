class UserCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.UserCountableEdge()
    totalCount = models.Int()

