class AppTokenVerify(models.Model):
    valid = models.Boolean()
    appErrors = models.AppError()

