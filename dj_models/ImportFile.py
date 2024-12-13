class ImportFile(models.Model):
    id = models.ID()
    user = models.User()
    app = models.App()
    status = models.JobStatusEnum()
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    message = models.String()
    url = models.String()
    events = models.ImportEvent()

