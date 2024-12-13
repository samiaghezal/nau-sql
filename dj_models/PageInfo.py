class PageInfo(models.Model):
    hasNextPage = models.Boolean()
    hasPreviousPage = models.Boolean()
    startCursor = models.String()
    endCursor = models.String()

