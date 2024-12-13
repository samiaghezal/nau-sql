class MenuItemCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.MenuItemCountableEdge()
    totalCount = models.Int()

