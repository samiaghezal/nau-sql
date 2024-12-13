class AppFetchManifest(models.Model):
    manifest = models.Manifest()
    appErrors = models.AppError()

