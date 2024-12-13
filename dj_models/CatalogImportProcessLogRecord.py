class CatalogImportProcessLogRecord(models.Model):
    id = models.ID()
    createdAt = models.DateTime()
    taskId = models.String()
    objectId = models.String()
    operation = models.CatalogImportProcessLogRecordOperation()
    relatedObjectName = models.String()

