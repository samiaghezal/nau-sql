class WarehouseCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.WarehouseCountableEdge()
    totalCount = models.Int()

