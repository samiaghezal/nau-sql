class EmailEventCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.EmailEventCountableEdge()
    totalCount = models.Int()

