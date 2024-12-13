class AppInstallation(models.Model):
    appName = models.String()
    manifestUrl = models.String()
    id = models.ID()
    status = models.JobStatusEnum()
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    message = models.String()

