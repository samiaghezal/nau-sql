class AppRetryInstall(models.Model):
    appErrors = models.AppError()
    appInstallation = models.AppInstallation()

