class AppUpdate(models.Model):
    appErrors = models.AppError()
    app = models.App()

