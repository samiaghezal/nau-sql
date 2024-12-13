class TenantCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.TenantCountableEdge()
    totalCount = models.Int()

