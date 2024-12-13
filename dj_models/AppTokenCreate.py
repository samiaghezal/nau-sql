class AppTokenCreate(models.Model):
    authToken = models.String()
    appErrors = models.AppError()
    appToken = models.AppToken()

