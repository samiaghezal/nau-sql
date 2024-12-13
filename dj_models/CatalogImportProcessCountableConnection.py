class CatalogImportProcessCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.CatalogImportProcessCountableEdge()
    totalCount = models.Int()

