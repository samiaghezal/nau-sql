class CatalogImportProcess(models.Model):
    status = models.CatalogImportProcessStatus()
    message = models.String()
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    taskId = models.String()
    externalSource = models.String()
    finishedAt = models.DateTime()
    createdBy = models.User()
    seller = models.Seller()
    internalNotes = models.String()
    id = models.ID()
    records = models.CatalogImportProcessLogRecordCountableConnection()

