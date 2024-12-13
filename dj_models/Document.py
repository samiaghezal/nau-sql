class Document(models.Model):
    id = models.ID()
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    tenant = models.Tenant()
    file = models.String()
    name = models.String()
    description = models.String()
    fileExtension = models.String()
    fileContentType = models.String()
    fileSize = models.FileSize()
    url = models.String()

