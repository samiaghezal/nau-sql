class CatalogImportProcessLogRecordCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.CatalogImportProcessLogRecordCountableEdge()
    totalCount = models.Int()

