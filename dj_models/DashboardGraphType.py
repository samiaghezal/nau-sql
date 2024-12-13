class DashboardGraphType(models.Model):
    filters = models.FilterObjectType()
    graph = models.GraphDataType()

