class PluginCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PluginCountableEdge()
    totalCount = models.Int()

