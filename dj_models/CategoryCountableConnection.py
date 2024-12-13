class CategoryCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.CategoryCountableEdge()
    totalCount = models.Int()

