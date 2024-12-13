class CatalogImportProcessLogRecordCountableEdge(models.Model):
    node = models.CatalogImportProcessLogRecord()
    cursor = models.String()

