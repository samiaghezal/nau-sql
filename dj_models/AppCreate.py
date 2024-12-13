class AppCreate(models.Model):
    authToken = models.String()
    appErrors = models.AppError()
    app = models.App()

