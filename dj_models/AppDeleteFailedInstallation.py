class AppDeleteFailedInstallation(models.Model):
    appErrors = models.AppError()
    appInstallation = models.AppInstallation()

